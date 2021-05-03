## DECODE
import sys
import PQHeap # Dette er gruppens PQHeap.py fra del I.
import bitIO
from Element import Element

n = 256

infile = open(sys.argv[1], 'rb')
bitstreamin = bitIO.BitReader(infile)
freq = []
numberofbytes = 0
bits = []
for i in range(n):
    freq.append(bitstreamin.readint32bits())
    numberofbytes += freq[i]
while True:
    x = bitstreamin.readbit()
    bits.append(x)
    if not bitstreamin.readsucces():  # End-of-file?
        break
bitstreamin.close()

#use PQHeap to create pq for frequencies
pq = PQHeap.createEmptyPQ()
for i in range(n):
    PQHeap.insert(pq, Element(freq[i], [i]))

#create Huffman tree
for i in range(0,n-1):
    x = PQHeap.extractMin(pq)
    y = PQHeap.extractMin(pq)
    z = Element(x.key+y.key, [x.data, y.data])
    PQHeap.insert(pq, z)
tree = PQHeap.extractMin(pq).data

outfile = open(sys.argv[2], 'wb')
i = 0
currentbytes = 0
while len(bits) > i:
    newtree = tree
    while not isinstance(newtree[0], int):
        if bits[i] == 1:
            newtree = newtree[1]
        if bits[i] == 0:
            newtree = newtree[0]
        i += 1
    outfile.write(bytes([newtree[0]]))
    currentbytes += 1
    if currentbytes == numberofbytes:
        break
outfile.close()
