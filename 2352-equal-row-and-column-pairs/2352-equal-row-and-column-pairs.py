class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rows = Counter(tuple(row) for row in grid)

        ans = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            ans += rows[col]

        return ans
