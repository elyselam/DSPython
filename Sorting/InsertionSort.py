#not optimal
def insertion_swap(A):
    #start at 1st item
    for i in range(1, len(A)):
        for j in range(i - 1, -1, -1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
        else:
            break
    return A

#optimized, shifts instead of swapping
def insertion_shift(A):
    for i in range(1, len(A)):
        curr = A[i]
        k = 0
        for j in range(i-1, -2, -1):
            k = j
            if A[j] > curr:
                A[j+1] = A[j]
            else:
                break
        A[k+1] = curr
    return A


A = [5,9,1,2,4,8,6,3,7]

print(insertion_swap(A))

print(insertion_shift(A))

