class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0
        if not needle:
            return 0
        
        # Use Python's built-in find (O(n*m) worst case)
        return haystack.find(needle)