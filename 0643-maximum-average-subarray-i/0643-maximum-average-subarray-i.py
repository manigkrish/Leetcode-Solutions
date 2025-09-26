class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # compute initial window sum (first k elements)
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # slide window from i = k to n-1
        for i in range(k, n):
            # remove nums[i-k], add nums[i]
            window_sum += nums[i] - nums[i - k]
            # update max_sum
            if window_sum > max_sum:
                max_sum = window_sum
        
        # max average is max_sum / k
        return max_sum / k
