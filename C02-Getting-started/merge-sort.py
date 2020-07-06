def merge(L, R):
    '''
    合并步骤
    '''
    n = len(L) + len(R)
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0
    j = 0
    A = []
    for k in range(0, n):
        if L[i]<=R[j]:
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1
    return A 

def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        left = 0
        right = len(A)
        mid =  (len(A))>>1
        left = merge_sort(A[0:mid])
        right = merge_sort(A[mid:])
    return merge(left, right)

print(merge_sort([4,3,5,7,8,2,2,3,443,12,567,3231,94]))