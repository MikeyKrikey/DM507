#asodifaosdjfo

# Side 152
def Parent(i):
    return i // 2

def Left(i):
    return 2*i

def Right(i):
    return 2*i + 1

# Side 154
def maxHeapify(A,i):
    l = Left(i)
    r = Right(i)

    if (l <= A.heapsize and A[l] > A[i]):
        largest = l
    else largest = i

    if (r <= A.heapsize and A[r] > A[largest]):
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A,largest)

# Side 163
def heapMaximum(A):
    return A[1]

def heapExtractMax(A):
    if A.heapsize < 1:
        ValueError('Heap underflow')
    
    maximum = A[1]
    A[1] = A[A.heapsize]
    A.heapsize = A.heapsize - 1
    maxHeapify(A,1)
    return maximum

# Side 164
def heapIncreaseKey(A,i,key):
    if key < A[i]:
        ValueError('new key is smaller than current key')
    
    A[i] = key

    while i > 1 and A[Parent[i]] < A[i]
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)

def maxHeapInsert(A,key):
    A.heapsize = A.heapsize + 1
    A[A.heapsize] = -infty
    heapIncreaseKey(A,A.heapsize,key)

# Vores implementering
def extractMin(A):
    # Fjerner det element med mindst prioritet i prioritetskøen A og returnerer det


def insert(A,e):
    # Indsætter elementet e i prioritetskøen A

def createEmptyPQ():
    # Returnerer en ny, tom prioritetskø (en tom liste)
  

