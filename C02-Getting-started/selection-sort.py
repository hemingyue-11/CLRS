def selection_sort(A):
    for i in range(len(A)-1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j 
        A[minIndex], A[i] = A[i], A[minIndex]
    return A 

A= [5,3,2,7,1,1]
print(selection_sort(A))
                
            
