#if lists are already sorted
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            sorted.append(left.pop(0))
        else:
            sorted.append(right.pop(0))
    #when list is empty and the other contains sorted val > than last el of the sorted list,
    # now we can just append both empty lists and other list to sorted variable
    sorted += left
    sorted += right
    return sorted


def mergeUnsorted(lst):
    if len(lst) < 2:
        return lst
    midpoint = len(lst)//2
    left = mergeUnsorted(lst[:midpoint])
    right = mergeUnsorted(lst[midpoint:])

    result = merge(left, right)
    return result


