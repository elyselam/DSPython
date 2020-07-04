# def balance_check(s):
#     if len(s) % 2 != 0:
#         return False
#
#     open = set('([{')
#
#     matches = set([ ('(',')'), ('[',']'), ('{','}') ])
#
#     stack = []
#     for p in s:
#         # if it's an opening p
#         if p in open:
#             stack.append(p)
#
#         else:
#             if len(stack) == 0:
#                 return False
#             last_open = stack.pop()
#
#             if (last_open, p) not in matches:
#                 return False
#
#     return len(stack) == 0 #return True bc empty stack means every matched

def balance_check(s):
    # Check is even number of brackets
    if len(s) % 2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')

    # Matching Pairs
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Use a list as a "Stack"
    stack = []

    # Check every parenthesis in string
    for paren in s:

        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)

        else:

            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False

            # Check the last open parenthesis
            last_open = stack.pop()

            # Check if it has a closing match
            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0

print(balance_check('()(){]}'))


def balancedBrackets(string):
    # Write your code here.
    opening = ["(", "{", "["]
    matched_pairs = {"(": ")", "{": "}", "[": "]"}
    # closing = [")", "}", "]"]
    openingStack = []

    for bracket in string:
        if bracket in opening:
            openingStack.append(bracket)
        else:
            #if bracket in first/last is not opening
            #and nothing in openingStack, then return false
            if bracket == string[0] or bracket == string[len(string)-1] and len(openingStack) == 0:
                return False

            lastBracketAdded = openingStack.pop()
            if bracket != matched_pairs[lastBracketAdded]:
                return False
        return len(openingStack) == 0