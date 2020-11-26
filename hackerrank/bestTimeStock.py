'''
Input: [7,1,5,3,6,4]
Output: 5

Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''
# O(n^2): nested loops, n is size of array
# O(1)
def max_prof_bruteforce(arr):
    max_prof = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            #rules out when el is larger than its next
            if arr[j] - arr[i] > max_prof:
                max_prof = arr[j] - arr[i]
    return max_prof


# print(max_prof_bruteforce([7,1,5,3,6,4]))




def max_profit(arr):

# [7, 1, 5, 3, 6, 4]
# cur_min
#     min
#     curProf = 4
#           min
#           curProf = 3
    if not arr:
        return 0

    max_prof = 0
    cur_min = arr[0]
    for i in range(1, len(arr)):
    # [7, 1, 5, 3, 6, 4]
    # cur_min = 7
        if arr[i] < cur_min:
            #now cur_min = 1
            cur_min = arr[i]

        max_prof = max(max_prof, arr[i] - cur_min)
    return max_prof

print(max_profit([7, 1, 5, 3, 6, 4]))



def max_pro(arr):
    if not arr:
        return 0
    buy = arr[0]
    prof = 0
    for i in arr[1:]:
        if (i - buy) > prof:
            prof = i - buy
        elif i < buy:
            buy = i
    return prof



print(max_pro([7, 1, 5, 3, 6, 4]))
