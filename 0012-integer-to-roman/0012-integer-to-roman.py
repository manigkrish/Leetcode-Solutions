class Solution:
    def intToRoman(self, num: int) -> str:
        # Roman numeral mappings
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        
        romans = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        result = []
        
        # Build Roman numeral by greedily subtracting
        for i, v in enumerate(values):
            while num >= v:
                num -= v
                result.append(romans[i])
        
        return "".join(result)