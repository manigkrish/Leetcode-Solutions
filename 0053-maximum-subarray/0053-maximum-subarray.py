import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        if all(n < 0 for n in nums):
            return max(nums)

        curr_sum = 0
        max_sum = -sys.maxsize - 1  

        for num in nums:
            curr_sum += num
            if curr_sum < 0:
                curr_sum = 0
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
