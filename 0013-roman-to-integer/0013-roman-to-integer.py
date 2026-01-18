class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        n = len(s)
        
        for i in range(n):
            value = roman_map[s[i]]
            
            # If this numeral is followed by a larger one, subtract it.
            if i + 1 < n and roman_map[s[i + 1]] > value:
                result -= value
            else:
                result += value
        
        return result
