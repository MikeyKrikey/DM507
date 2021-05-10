'''
Gruppe:

Stine Holz Meinhardt Gregersen, sgreg18
Michael Kristensen, mickr19
Hanna Bruun-Schmidt, habru19

'''

## DECODE
import sys
import PQHeap # Dette er gruppens PQHeap.py fra del I.
import bitIO
from Element import Element

#number of bytes
n = 256

#read file to create list of frequencies and list of encoded data
infile = open(sys.argv[1], 'rb')
bitstreamin = bitIO.BitReader(infile)
freq = []
numberofbytes = 0
bits = []
#append each integer to the list of frequencies
for i in range(n):
    freq.append(bitstreamin.readint32bits())
    numberofbytes += freq[i] #count total number of bytes from original file
#append each element of encoded data
while True:
    x = bitstreamin.readbit()
    bits.append(x)
    if not bitstreamin.readsucces():
        break
bitstreamin.close()

#use PQHeap to create pq for frequencies
pq = PQHeap.createEmptyPQ()
for i in range(n):
    PQHeap.insert(pq, Element(freq[i], [i])) #we use the given class "element"

#create Huffman tree, as in "ENCODE"
for i in range(0,n-1):
    x = PQHeap.extractMin(pq)
    y = PQHeap.extractMin(pq)
    z = Element(x.key+y.key, [x.data, y.data])
    PQHeap.insert(pq, z)
tree = PQHeap.extractMin(pq).data

#open outputfile
outfile = open(sys.argv[2], 'wb')
i = 0
currentbytes = 0
while len(bits) > i:
    newtree = tree #create new tree for recursive run-through
    while not isinstance(newtree[0], int): #while 0 element is not an integer, it is not at the root
        if bits[i] == 1: #move to the right in the Huffman tree
            newtree = newtree[1] 
        if bits[i] == 0: #move to the left in the Huffman tree
            newtree = newtree[0]
        i += 1
    #write decoded byte from current code
    outfile.write(bytes([newtree[0]]))
    currentbytes += 1
    #end when we have written original number of bytes to outputfile
    if currentbytes == numberofbytes:
        break
outfile.close()
