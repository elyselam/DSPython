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

# https://www.youtube.com/watch?v=kZH0vWXs_Bk&ab_channel=Amigoscode



''' 4 9 3 6 2
4 is min, 9 is i
is 4 < 9? yes => 4 stays as min
is 4 < 3? no => 3 is now min

is 3 < 6? yes => 3 stays as min
is 3 < 2? no => 2 is now min
2 swaps with 4 :) now it's sorted from the left 

'''