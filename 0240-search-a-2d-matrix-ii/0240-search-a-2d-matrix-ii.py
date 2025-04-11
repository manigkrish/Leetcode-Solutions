class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        no_rows = len(matrix)
        no_cols = len(matrix[0])

        # Check boundaries
        if target < matrix[0][0] or target > matrix[no_rows - 1][no_cols - 1]:
            return False

        # Start from top-right corner
        r, c = 0, no_cols - 1

        while r < no_rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1

        return False
