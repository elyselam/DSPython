import collections
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")
#
# x = zip(a, b)
#
# #use the tuple() function to display a readable version of the result:
#
# print(x)
#
# print(type(x))
from sys import maxsize


def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    # otherwise return last ele
    return arr1[-1]


def finder2(arr1,arr2):
    d=collections.defaultdict(int)

    # add 1 to every instance in arr1
    for i in arr2:
        d[i] += 1
    #defaultdict(<type 'int'>, {5: 1, 7: 2})

    for i in arr1:
        if d[i] == 0:
            return i
        else:
            d[i] -= 1

arr1 = [5,5,7,7]
arr2 = [5,7,7]

# print(finder2(arr1,arr2)) #5



#find largest sum before sum goes negative
def large_cont_sum(arr):
    if len(arr)==0:
        return 0
    max_sum = curr_sum = arr[0]
    for i in arr[1:]:
        curr_sum = max(curr_sum + i, i)
        print(curr_sum, 'curr')
        max_sum = max(curr_sum, max_sum)
        print(max_sum, 'max')
    return max_sum


print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1])) #29




# def large_cont_sum1(arr):
#     max_sum = -maxsize -1
#     max_ending_here = 0
#     start = 0
#     end = 0
#     new_start = 0
#     for i in range(0, len(arr)):
#         max_ending_here += arr[i]
#         if max_ending_here > max_sum:
#             max_sum = max_ending_here
#             start = new_start
#             end = i
#         if max_ending_here < 0:
#             max_ending_here = 0
#             new_start = i + 1
#         return (max_sum, arr[start:end+1])
# print(large_cont_sum1([1,2,-1,3,4,10,10,-10,-1])) #29



#O(n) time | O(1) space
def isValidSubsequence(arr, seq):
    arr_i = 0
    seq_i = 0
    while arr_i < len(arr) and seq_i < len(seq):
        if arr[arr_i] == seq[seq_i]:
            seq_i +=1 #only moves along if found a match
        arr_i +=1

    return seq_i == len(seq) #only True if seq_i has reached the end

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])) #True








def isValidSub(arr, arr2):
    arr_i = arr2_i = 0
    while arr_i < len(arr) and arr2_i < len(arr2):
        if arr[arr_i] == arr2[arr2_i]:
            arr2_i += 1
        arr_i += 1
    return arr2_i == len(arr2)


print(isValidSub([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))  # True


# seq has to be in order to main arr
#O(n) because has to iterate through the whole main arr

def isValidSubsequence1(arr, seq):
    seq_i = 0
    for i in arr:
        # if seq_i == len(seq):
        #     return True
        if seq[seq_i] == i:
            seq_i += 1
    return seq_i == len(seq)

print(isValidSubsequence1([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])) #True



#
# def fib(n):
#     result = [0,1]
#     for i in range(2, n):
#         a = result[i-1]
#         b = result[i-2]
#         print(i)
#         result.append(a+b)
#         print(len(result))
#     return result[n+1]
# print(fib(5))

def fibRec(n):
    if n <= 2:
        return n
    return fibRec(n-1) + fibRec(n-2)
print(fibRec(5))






fib_cache = {}

def fib(n):
    #if already cached value, then return it
    if n in fib_cache:
        return fib_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    else:
        value = fib(n-1) + fib(n-2)
    fib_cache[n] = value
    return value

for n in range(1,11):
    print(n, ":", fib(n))




# from functools import lru_cache
#
# @lru_cache(maxsize=1000)
# def fib1(n):
#     #check if input is a positive int
#     if type(n) != int:
#         raise TypeError("n must be a positive int")
#     if n < 1:
#         raise ValueError("n must a positive int")
#
#     if n <= 2:
#         return 1
#     return fib1(n-1) + fib1(n-2)



