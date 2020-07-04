def insertion(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap(j, j-1, arr)
            j -= 1
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

print(insertion([8,5,2,9,5,6,3]))




def insertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        prevIdx = i-1
        #swap if
        while prevIdx >= 0 and arr[prevIdx] > curr:
            arr[prevIdx + 1] = arr[prevIdx]
            prevIdx -= 1
        arr[prevIdx + 1] = curr
    return arr

# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         curr = arr[i]
#         prev = arr[i-1]
#         #swap if
#         while prevIdx >= 0 and prev > curr:
#             arr[prevIdx + 1] = prev
#             prevIdx -= 1
#         arr[prevIdx + 1] = curr
#     return arr


# print(insertionSort([8,5,2,9,5,6,3]))


def insertion_sort(arr):
    # We start from 1 since the first element is trivially sorted
    for i in range(1, len(arr)):
        curr = arr[i]
        currI = i

        # if haven't reached the beginning
        # and there is an element in our sorted arr > the one we're trying to insert
        while currI > 0 and arr[currI - 1] > curr:
            # swap it to the right
            arr[currI] = arr[currI -1]
            currI = currI - 1


        # We have either reached the beginning of the arr or we have found
        # an element of the sorted arr that is smaller than the element
        # we're trying to insert at i currI - 1.
        # Either way - we insert the element at currI
        arr[currI] = curr
    return arr

print(insertion_sort([8,5,2,9,5,6,3]))