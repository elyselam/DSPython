def unique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
        return True

#worst O(n log n)
#best: O(n)
def unique2(s):
    temp = sorted(s)
    for i in range(1, len(temp)):
        if s[i-1] == s[i]:
            return False
    return True
