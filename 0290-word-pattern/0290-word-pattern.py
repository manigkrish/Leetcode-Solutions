class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if pattern is None or s is None:
            return False

        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        lookup = {}

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in lookup:
                if lookup[p] != w:
                    return False
            else:
                if w in lookup.values():  
                    return False
                lookup[p] = w

        return True
if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    soln = Solution()
    print(soln.wordPattern(pattern, s))  
