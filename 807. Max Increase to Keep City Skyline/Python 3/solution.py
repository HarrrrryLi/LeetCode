class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])
        left = [max(row) for row in grid]
        top = []
        for col in zip(*grid):
            top.append(max(col))

        result = 0
        for r in range(row_size):
            row_max = left[r]
            for c in range(col_size):
                col_max = top[c]
                result += max(0, min(col_max, row_max) - grid[r][c])

        return result
