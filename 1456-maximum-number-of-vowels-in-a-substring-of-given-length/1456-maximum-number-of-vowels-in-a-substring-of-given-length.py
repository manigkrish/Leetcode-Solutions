class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        # count vowels in the first window of size k
        cnt = sum(1 for c in s[:k] if c in vowels)
        max_cnt = cnt
        
        # slide window
        for i in range(k, len(s)):
            # add the new character at i
            if s[i] in vowels:
                cnt += 1
            # remove the character leaving the window at i-k
            if s[i - k] in vowels:
                cnt -= 1
            # update max
            if cnt > max_cnt:
                max_cnt = cnt
        
        return max_cnt
