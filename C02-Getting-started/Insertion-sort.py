def insertion_sort(A):
    '''
    插入排序（升序）
    '''
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


def insertion_sort2(A):
    '''
    插入排序（降序）
    '''
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j]<key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key 
    return key 
