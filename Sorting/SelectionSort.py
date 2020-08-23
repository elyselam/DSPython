nums = [4,9,3,6,2]

def selection(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            #if curr < min
            if arr[j] < arr[min_i]:
                #min is now curr
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

print(selection(nums))