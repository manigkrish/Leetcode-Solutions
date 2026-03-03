class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: n == 1 always has string "0"
        if n == 1:
            return "0"
        
        # Length of S_n is 2^n - 1
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        # If k points to the middle of S_n, that bit is "1"
        if k == mid:
            return "1"
        
        # If k is in the left half, it's same as S_(n-1)
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        # If k is in the right half:
        # Find corresponding position in S_(n-1) symmetrically,
        # then invert the bit.
        mirror_pos = length - k + 1
        bit = self.findKthBit(n - 1, mirror_pos)
        
        return "1" if bit == "0" else "0"