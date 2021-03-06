import math

'''
Gruppe:

Stine Holz Meinhardt Gregersen, sgreg18
Michael Kristensen, mickr19
Hanna Bruun-Schmidt, habru19

'''

# Side 152 (skiftede til definerede)
def Parent(i):
    return math.floor((i-1) / 2)

def Left(i):
    return 2*i + 1

def Right(i):
    return 2*i + 2

# min-heapify
def minHeapify(A,i):
    l = Left(i)
    r = Right(i)

    if (l <= len(A)-1 and A[l] < A[i]):
        smallest = l
    else:
        smallest = i

    if (r <= len(A)-1 and A[r] < A[smallest]):
        smallest = r
    
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A,smallest)

# Vores implementering
def extractMin(A):
    minimum = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    minHeapify(A,0)
    return minimum

def insert(A,e):
    A.append(e)
    i = len(A) - 1
    while i > 0 and A[Parent(i)] > A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)

def createEmptyPQ():
    return []
    