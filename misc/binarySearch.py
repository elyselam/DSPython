


def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        m = (left + right) //2

        potentialMatch = arr[m]
        if target == potentialMatch:
            return m
        elif target <= potentialMatch:
            right = m - 1
        else:
            left = m + 1

    return -1



print(binarySearch([0,1,21,33,45,45,61,71,72,73], 33))