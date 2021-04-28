## ENCODE
import sys
import PQHeap # Dette er gruppens PQHeap.py fra del I.
import bitIO
from Element import Element


file = open(sys.argv[1], 'rb')
freq = [0] * 256
b = file.read(1)
while b != b'':
    freq[b[0]] += 1
    b = file.read(1)
file.close()

pq = PQHeap.createEmptyPQ()

for i in range(256):
    PQHeap.insert(pq, Element(freq[i], [i]))

n = 256

for i in range(0,n-1):
    x = PQHeap.extractMin(pq)
    y = PQHeap.extractMin(pq)
    z = Element(x.key+y.key, [x.data, y.data])
    PQHeap.insert(pq, z)
tree = PQHeap.extractMin(pq).data

def orderedTraversal(tree, kode = "", table = []):
    if isinstance(tree[0], list):
        orderedTraversal(tree[0], kode + "0", table)
        orderedTraversal(tree[1], kode + "1", table)
    elif isinstance(tree[0], int):
        table.append([tree[0], kode])
    return tree[0]
table = []
orderedTraversal(tree, "", table)
print(table)

file = open(sys.argv[1], 'rb')
numbers = []
b = file.read(1)
while b != b'':
    numbers.append(b[0])
    b = file.read(1)
file.close()

for i in numbers:
    for j in table:
        if i == j[0]:
            print(j[1])
            break
