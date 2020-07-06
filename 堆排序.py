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
        else:
            return A

def build_max_heap(A, heap_size):
    '''
    建立一个最大堆
    '''
    for i in range((heap_size>>1)-1, -1, -1):
        max_heapify(A, i, heap_size)
    return A

def heapsort(A):
    '''
    堆排序算法
    '''
    heap_size = len(A)
    build_max_heap(A, heap_size)
    for i in range(len(A)-1, 0, -1):
        maxnum = A[0]
        A[0] = A[i]
        A[i] = maxnum
        heap_size -= 1
        max_heapify(A, 0, heap_size)
    return A



