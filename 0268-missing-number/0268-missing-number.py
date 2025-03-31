class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        xor_nums = 0
        xor_full_range = 0
        for num in nums:
            xor_nums ^= num

        for i in range(len(nums) + 1):
            xor_full_range ^= i

        return xor_nums ^ xor_full_range