'''
Gruppe:

Stine Holz Meinhardt Gregersen, sgreg18
Michael Kristensen, mickr19
Hanna Bruun-Schmidt, habru19

'''

## ENCODE
import sys
import PQHeap # Dette er gruppens PQHeap.py fra del I.
import bitIO
from Element import Element

#number of bytes
n = 256

#read file to create list of frequencies
infile = open(sys.argv[1], 'rb')
freq = [0] * n
b = infile.read(1)
#increase list of frequencies, for each observed byte
while b != b'':
    freq[b[0]] += 1
    b = infile.read(1)
infile.close()

#use PQHeap to create pq for frequencies
pq = PQHeap.createEmptyPQ()
for i in range(n):
    PQHeap.insert(pq, Element(freq[i], [i])) #we use the given class "element"

#create Huffman tree by using priority queue
for i in range(0,n-1):
    x = PQHeap.extractMin(pq) #exstract the minimum elements of current PQ
    y = PQHeap.extractMin(pq)
    z = Element(x.key+y.key, [x.data, y.data])
    PQHeap.insert(pq, z) #insert element z, which is a combination of the two minimum elements
tree = PQHeap.extractMin(pq).data #the data of the root of the tree will contain the Huffman tree

#create table of codes from tree by use of "ordered traversal", which goes through every "leaf" of the tree
def orderedTraversal(tree, kode = "", table = []):
    if isinstance(tree[0], list): #if element 0 is list, then it is not a leaf
        orderedTraversal(tree[0], kode + "0", table) #when going left into the tree, we append "0" to the code
        orderedTraversal(tree[1], kode + "1", table) #when going right into the tree, we append "1" to the code
    elif isinstance(tree[0], int): #if element 0 is an integer, it is a leaf
        table.append([tree[0], kode]) #create table with current code
    return tree[0]
table = []
orderedTraversal(tree, "", table)

#read file again for list of bytes in inputfile
infile = open(sys.argv[1], 'rb')
byte = []
b = infile.read(1)
#append next byte to list
while b != b'':
    byte.append(b[0])
    b = infile.read(1)
infile.close()

#write bits in terms of Huffman coding
outfile = open(sys.argv[2], 'wb')
bitstreamout = bitIO.BitWriter(outfile)
#print frequencies
for i in range(n):
    bitstreamout.writeint32bits(freq[i])
#print each bit translated via huffman encoding
for i in byte:
    for j in table:
        if i == j[0]:
            for k in range(0, len(j[1])):
                bitstreamout.writebit(int(j[1][k]))
bitstreamout.close()
