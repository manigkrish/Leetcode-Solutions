class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer to track the position of the last non-zero element
        last_non_zero_index = 0
        
        # Move all non-zero elements to the beginning of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                if i != last_non_zero_index:
                    nums[i] = 0
                last_non_zero_index += 1
