"""Given:

'This is the best'

Return:

'best the is This' """

def rev_word1(s):
    str = " "
    for i in s:
        str = i + str
    return str

def rev_word2(s):
    return " ".join(reversed(s.split()))
    # return " ".join(s.split()[::-1])

# print(rev_word2("hi buttface")) #buttface hi

def rev_words_recursive(s):
    if len(s) == 0:
        return s
    else:
        return rev_words_recursive(s[1:]) +s[0]


print(rev_words_recursive("hi buttface"))

# def rev_word3(s):
#     words = []
#     spaces = [" "]
#     for i in range(len(s)):
#         if s[i] not in [" "]:


# def rev_word3(s):
#     res = []
#     spaces = [' ']
#     i = 0
#
#     while i < len(s):
#         #starts iterating where not a space
#         if s[i] not in spaces:
#             first_word_start = i
#
#         while i < len(s) and s[i] not in spaces:
#             i += 1
#
#         res.append(s[first_word_start:i])
#     i += 1
#     return " ".join(reverse(res))
#
# rev_word3('   Hello John    how are you   ')






def compress(s):
    res = ""
    # if len(s) == 0:
    #     return ""
    # if len(s) == 1:
    #     return s + "1"
    count = 1
    res += s[0]

    for i in range(len(s) - 1):
        if s[i] == s[i+1]: #if consecutive char is same, keep counting
            count += 1
        else:
            if count > 1:
                #ignore if no repeats
                res += str(count)
                print(res + "  count is over 1")
                print(count)
            res += s[i+1]
            count = 1 #resets back to 1
    if count > 1:
        res += str(count)
    return res
print(compress("a"))
print(compress('AA'))
print(compress('mississippi'))


def get_largest_item(items):
    largest = float('-inf')
    for item in items:
        if item > largest:
            largest = item
    return largest
print(get_largest_item([1,2,3]))


