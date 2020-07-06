def partition(A, left, right):
    x = A[right]
    i = left-1
    for j in range(left, right):
        if A[j]<=x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[right] = A[right], A[i+1]
    return i+1

def quicksort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quicksort(A, left, q-1)
        quicksort(A, q+1, right)
    return A 
A = [5,3,1,7,9,12]
print(quicksort(A, 0, len(A)-1))