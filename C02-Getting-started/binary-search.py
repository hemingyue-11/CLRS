def binary_search(A, key):
    left = 0
    right = len(A)-1
    while left<=right:
        mid = (left+right)>>1
        if A[mid] == key:
            return mid 
        elif A[mid] < key:
            left = mid+1
        else:
            right = mid

A = [1,3,5,6,8,9,22,44,66]
print(binary_search(A, 1))
