Test

hej

def HeapMaximum(A):
    return A[1]
  
def HeapExtractMax(A):
    if A.heapsize < 1:
        ValueError('Heap underflow')
    
    max = A[1]
    A[1] = A[A.heapsize]
    A.heapsize = A.heapsize - 1
    MaxHeapify(A,1)
    return max
  

