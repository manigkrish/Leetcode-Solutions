class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        solutions = [-1] * (n + 1)  # Initialize with n+1 to handle n=0 and n=1
        return self.numUniqueBST(n, solutions)

    def numUniqueBST(self, n, solutions):
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        if solutions[n] != -1:  # If already computed, return the stored value
            return solutions[n]
        
        possibilities = 0
        for i in range(1, n+1):  # Iterate from 1 to n
            left = self.numUniqueBST(i-1, solutions)
            right = self.numUniqueBST(n-i, solutions)
            possibilities += left * right
        
        solutions[n] = possibilities  # Store the computed value
        return possibilities