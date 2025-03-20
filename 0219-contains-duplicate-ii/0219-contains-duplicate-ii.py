class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False  

        index_dict = {} 

        for i, num in enumerate(nums):
            if num in index_dict and i - index_dict[num] <= k:
                return True  
            index_dict[num] = i  

        return False  

        