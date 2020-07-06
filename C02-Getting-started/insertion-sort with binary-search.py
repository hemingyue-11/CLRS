def insertion_sort_with_binarysearch(A):
    for i in range(1,len(A)):
        key = A[i]
        left = 0
        right = i-1
        while left <= right:
            mid = (left+right)>>1
            if A[mid]<=key:
                left = mid+1
            if A[mid]>= key:
                right = mid-1
        j = i-1
        print(i, left)
        print(A)
        while j >= left:
            A[j+1] = A[j]
            j -= 1
        A[left] = key
    return A


A = [4,3,2,123,334,5,432,146,7654,456,5,4,2,1,6,5,4,7]
print(insertion_sort_with_binarysearch(A))