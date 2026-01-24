class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize closest sum to something far from target
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If this sum is closer to target than our previous best, update
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers based on comparison to target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If exact match, we can return immediately
                    return target
        return closest_sum