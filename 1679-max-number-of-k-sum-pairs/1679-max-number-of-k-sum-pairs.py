from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operations = 0
        
        for num in count:
            complement = k - num
            if complement == num:
                operations += count[num] // 2
            elif complement > num:
                operations += min(count[num], count[complement])
        
        return operations
