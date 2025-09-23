class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words (handles multiple spaces automatically)
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words into a single string separated by a space
        return ' '.join(reversed_words)
