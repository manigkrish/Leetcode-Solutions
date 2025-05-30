class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while(b!=0):
            temp= (a&b)<<1
            a=(a^b) & mask
            b=temp & mask
        return a if a<=max_int else ~(a^mask)