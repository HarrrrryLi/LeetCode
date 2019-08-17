class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x_size = len(grid)
        y_size = len(grid[0])
        total = 0
        y_max = [0] * x_size
        for x in range(x_size):
            total += max(grid[x])
            for y in range(y_size):
                if grid[x][y]:
                    total += 1
                y_max[y] = max(y_max[y], grid[x][y])

        total += sum(y_max)
        return total
