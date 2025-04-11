class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        elif n == 1:
            return [[1]]

        r, c = n, n  
        k, l = 0, 0  
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        count = 1

        while k < r and l < c:
            for i in range(l, c):
                matrix[k][i] = count
                count += 1
            k += 1

            for i in range(k, r):
                matrix[i][c - 1] = count
                count += 1
            c -= 1

            if k < r:
                for i in range(c - 1, l - 1, -1):
                    matrix[r - 1][i] = count
                    count += 1
                r -= 1

            if l < c:
                for i in range(r - 1, k - 1, -1):
                    matrix[i][l] = count
                    count += 1
                l += 1

        return matrix
