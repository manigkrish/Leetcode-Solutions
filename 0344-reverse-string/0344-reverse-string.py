class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        current_str = list(s) 
        i, j = 0, len(s) - 1

        while i < j:
            current_str[i], current_str[j] = current_str[j], current_str[i]
            i += 1
            j -= 1

        return "".join(current_str)  
