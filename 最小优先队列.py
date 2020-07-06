def min_heapity(A, i, heap_size):
    while True:
        L = 2 * i + 1
        R = 2 * i + 2
        if L < heap_size and A[L] < A[i]:
            smallest = L
        else:
            smallest = i
        if R < heap_size and A[R] < A[smallest]:
            smallest = R
        if smallest != i:
            
            A[i], A[smallest]  = A[smallest], A[i] 
  
            i = smallest
        else:
            return A

def build_min_heap(A):
    heap_size = len(A)
    for i in range((heap_size-1)>>1, -1, -1):
        min_heapity(A, i, heap_size)
    return A

def minimum(A):
    return A[0]

def extract_min(A):
    min = A[0]
    A[0] = A[-1]
    heap_size = len(A)-1
    min_heapity(A, 0, heap_size)
    return min

def decrease_key(A, i, key):
    if key > A[i]:
        print("error")
    A[i] = key
    while i>0 and A[i] < A[(i-1)>>1]:
        A[(i-1)>>1], A[i] = A[i], A[(i-1)>>1]
        i = (i-1)>>1
    return A

def insert(A, key):
    A.append(float("inf"))
    decrease_key(A, len(A)-1, key)
    return A

