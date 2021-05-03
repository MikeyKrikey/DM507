## ENCODE
import sys
import PQHeap # Dette er gruppens PQHeap.py fra del I.
import bitIO
from Element import Element

n = 256

#read file to create list of frequencies
infile = open(sys.argv[1], 'rb')
freq = [0] * n
b = infile.read(1)
while b != b'':
    freq[b[0]] += 1
    b = infile.read(1)
infile.close()

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

#create table of codes from tree
def orderedTraversal(tree, kode = "", table = []):
    if isinstance(tree[0], list):
        orderedTraversal(tree[0], kode + "0", table)
        orderedTraversal(tree[1], kode + "1", table)
    elif isinstance(tree[0], int):
        table.append([tree[0], kode])
    return tree[0]
table = []
orderedTraversal(tree, "", table)

#read file again for list of bits in inputfile
infile = open(sys.argv[1], 'rb')
bits = []
b = infile.read(1)
while b != b'':
    bits.append(b[0])
    b = infile.read(1)
infile.close()

#write bits in terms of Huffman coding
outfile = open(sys.argv[2], 'wb')
bitstreamout = bitIO.BitWriter(outfile)
for i in range(n):
    bitstreamout.writeint32bits(freq[i])
for i in bits:
    for j in table:
        if i == j[0]:
            for k in range(0, len(j[1])):
                bitstreamout.writebit(int(j[1][k]))
bitstreamout.close()
