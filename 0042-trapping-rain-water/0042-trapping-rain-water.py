class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0

        maxseenright = 0
        maxseenright_arr = [0] * len(height)
        maxseenleft = 0
        rainwater = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > maxseenright:
                maxseenright = height[i]
            maxseenright_arr[i] = maxseenright

        for i in range(len(height)):
            water_level = min(maxseenright_arr[i], maxseenleft)
            rainwater += max(water_level - height[i], 0)
            if height[i] > maxseenleft:
                maxseenleft = height[i]

        return rainwater
