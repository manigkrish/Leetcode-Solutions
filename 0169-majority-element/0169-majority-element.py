class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = self.get_candidate(nums)
        candidate_count = 0

        if candidate is not None:
            for num in nums:
                if num == candidate:
                    candidate_count += 1

            if candidate_count > len(nums) // 2:  
                return candidate
        
        return None  

    def get_candidate(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        return candidate  
