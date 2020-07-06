def add_binary(A, B):
    '''
    把两个n位二进制整数加起来
    '''
    C = [0 for _ in range(len(A)+1)]
    carry = 0
    for i in range(len(A)-1, -1, -1):
        C[i+1] = (A[i]+B[i]+carry) % 2
        carry = (A[i]+B[i]+carry) // 2
    C[i] = carry 
    return C

def add_ten(A, B):
    carry = 0
    C = [0 for _ in range(len(A)+1)]
    for i in range(len(A)-1, -1, -1):
        C[i+1] = (A[i]+B[i]+carry) % 10
        carry = (A[i]+B[i]+carry) // 10
    C[i] = carry
    return C
print(add_ten([2, 5, 6, 7], [4, 3, 6, 7]))
