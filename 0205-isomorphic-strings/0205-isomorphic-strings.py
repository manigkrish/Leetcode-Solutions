class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
        if s == "" and t == "":
            return True
        if len(s) != len(t):
            return False

        lookup = {}
        mapped_values = set()

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in lookup:
                if lookup[c1] != c2:
                    return False
            else:
                if c2 in mapped_values:
                    return False
                lookup[c1] = c2
                mapped_values.add(c2)

        return True
