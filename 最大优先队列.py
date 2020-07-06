def max_heapify(A, i, heap_size):
    '''
    维护最大堆：假设Left(i)和Right(i)的二叉树都是最大堆，然是两个子树的父亲A[i]有可能小于其孩子，
    此算法通过让A[i]逐级下降，从而让A[i]根节点满足最大堆的性质
    :param  A:输入一个数组，即维护的最大堆
            i:根节点的位置
            heap_size:最大堆内的数据长度
    :out 维护后的数组（最大堆）
    
    时间复杂度：O(lgn)
    '''
    while 1:
        L = 2 * i + 1
        R = 2 * i + 2

        if L <= heap_size-1 and A[L] > A[i]:
            largest = L
        else:
            largest = i
        if R <= heap_size-1 and A[R] > A[largest]:
            largest = R
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            return A

def build_max_heap(A, heap_size):
    '''
    建立一个最大堆
    '''
    for i in range((heap_size>>1)-1, -1, -1):
        max_heapify(A, i, heap_size)
    return A


def maximum(A):
    return A[0]

def extract_max(A, heap_size):
    if len(A)<1:
        print("error")
    max = A[0]
    print(A)
    A[0] = A[heap_size-1]
    print(A)
    heap_size -= 1
    max_heapify(A, 0, heap_size)
    print(A)
    return max

def increast_key(A, i, key):
    if key < A[i]:
        print("error")
    while i>0 and key>A[(i-1)>>1]:
        A[i] = A[(i-1)>>1]
        i = (i-1)>>1
    A[i] = key
    return A

def insert(A, x):
    heap_size = len(A)
    heap_size += 1
    A.append(-float("inf"))
    increast_key(A, heap_size-1, x)

A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
build_max_heap(A, len(A))
extract_max(A, len(A))
