class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if adjacent plots are also empty
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  # Plant a flower
                    count += 1
                    if count >= n:
                        return True
                    i += 1  # Skip the next plot to maintain the no-adjacent-flowers rule
            i += 1
        return count >= n
