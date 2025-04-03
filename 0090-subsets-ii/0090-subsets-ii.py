class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  
        n = 1 << len(nums)  
        result = set()

        for i in range(n):
            subset = self.convert(i, nums)
            result.add(tuple(subset))  

        return [list(t) for t in result]

    def convert(self, i, nums):
        k = i
        index = 0
        res = []
        while k > 0:
            if k & 1:
                res.append(nums[index])
            k >>= 1
            index += 1
        return sorted(res)  
