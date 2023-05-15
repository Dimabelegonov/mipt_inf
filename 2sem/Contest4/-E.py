def heapsort(A):
    maxheap(A)
    print(A)

    for i in range(len(A)//2 - 1, -1, -1):
        heapyfy(A)


def maxheap(A):
    for i in range(len(A)):
        shift_down(A, i)


def shift_down(A, i):
    if i == 0:
        return
    parent_i = (i - 1) // 2
    if A[i] > A[parent_i]:
        A[i], A[parent_i] = A[parent_i], A[i]
        shift_down(A, parent_i)


def shift_up(A, i):
    if i == 0:
        return
    parent_i = (i - 1) // 2
    if A[i] < A[parent_i]:
        A[i], A[parent_i] = A[parent_i], A[i]
        shift_up(A, parent_i)


heapsort([3, 2, 5, 0, -1,6,7])
