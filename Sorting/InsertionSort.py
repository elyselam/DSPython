# #not optimal
# def insertion_swap(A):
#     #start at 1st item
#     for i in range(1, len(A)):
#         for j in range(i - 1, -1, -1):
#             if A[j] > A[j + 1]:
#                 A[j], A[j + 1] = A[j + 1], A[j]
#         else:
#             break
#     return A
#
# #optimized, shifts instead of swapping
# def insertion_shift(A):
#     for i in range(1, len(A)):
#         curr = A[i]
#         k = 0
#         for j in range(i-1, -2, -1):
#             k = j
#             if A[j] > curr:
#                 A[j+1] = A[j]
#             else:
#                 break
#         A[k+1] = curr
#     return A
#
#
# A = [5,9,1,2,4,8,6,3,7]
#
# print(insertion_swap(A))
#
# print(insertion_shift(A))


# def insert(arr):
#     for i in range(1, len(arr)):
#         curr = arr[i]
#         j = i - 1
#         while j >= 0:
#             if curr < arr[j]:
#                 #shift one spot to right
#                 arr[j+1] = arr[j]
#                 arr[j] = curr #shift value left into slot
#                 i=i-1
#             else:
#                 break
#



def insert(arr):
    for i in range(1, len(arr)):
        val_to_sort = arr[i]
        while arr[i-1] > val_to_sort and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr



print(insert([1,5,3,6,4]))


# CLRS:
def insertion(arr):
    for j in range(1, len(arr)):
        ''' loop invariant: at the start of each iteration of loop: 
        subarryay a[0..j-2] consists of elements originally in arr but sorted'''

        #set key to current item being moved into place
        key = arr[j]
        #i is item to left of j
        i = j - 1

        #within while loop, if prev_val > key, and index is not 0, then swap
        while arr[i] > key and i > 0:
            arr[i+1] = arr[i] #swap
            #keep comparing to prev items until reaching last item
            i = i - 1
        #once while loop breaks, i = 0, so the item at index 0 is assigned value of key
        arr[i+1] = key
    return arr


print(insertion([1,5,3,6,4]))