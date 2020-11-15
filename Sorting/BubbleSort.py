#sorted from tail

#bubble up, the largest number moves to the right
nums = [6,4,5,3,2]
#       0 1 2 3 4
def bubbleSort(arr):
    for i in range(len(arr)-1):
        # subtract i bc we know it's sorted from right side each iteration
        for j in range(len(arr)-1-i):

            # is 6 > 4?, swap
            # is 6 > 5?, swap
            # is 6 > 3?, swap
            # is 6 > 2?, swap arr[3]>arr[4]
            # [4,5,3,2,6]

            # is 4 > 5?, no

            # is 5 > 3?, swap
            # is 5 > 2?, swap. don't need to compare to 6 again arr[2]>arr[4]
            # [4,3,2,5,6]

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubbleSort(nums))