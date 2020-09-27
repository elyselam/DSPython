search_list = ['apple', 'orange', 'pear', 'fig', 'passionfruit']


def search(str, term, index=0):
    if str[0] == term:
        return index
    if len(str) <= 1:
        return -1
    return search(str[1:], term, index=index+1)

print(search(search_list, 'apple'))


f = open('random_int.txt', 'r')
ints = [int(line) for line in f.readlines()]

def summation(val):
    if len(val) == 0:
        return 0
    if len(val) == 1:
        return val[0]
    midpoint = len(val)//2
    return summation(val[:midpoint]) + summation(val[midpoint:])

print(summation(ints))
