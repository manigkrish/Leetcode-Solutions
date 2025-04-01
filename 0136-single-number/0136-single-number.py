class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None 

        xor_prod = 0
        for num in nums:
            xor_prod ^= num  

        return xor_prod
