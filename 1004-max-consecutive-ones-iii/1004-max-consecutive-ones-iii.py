from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If too many zeros in the window, shrink from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Now window [left..right] has at most k zeros
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        
        return max_len
