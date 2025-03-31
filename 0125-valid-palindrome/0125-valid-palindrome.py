import re

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        s = s.lower()
        newS = re.sub(r"[^a-z0-9]", "", s)
        start = 0
        end = len(newS) - 1
        while start < end:
            if newS[start] != newS[end]:
                return False
            start += 1
            end -= 1

        return True
