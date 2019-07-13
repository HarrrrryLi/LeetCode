class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])
        result = 0

        for row_cnt in range(row_size):
            for col_cnt in range(col_size):
                height = grid[row_cnt][col_cnt]
                area = height * 6
                area -= max(0, (height - 1)) * 2
                if row_cnt - 1 >= 0:
                    area -= min(height, grid[row_cnt - 1][col_cnt])
                if row_cnt + 1 < row_size:
                    area -= min(height, grid[row_cnt + 1][col_cnt])
                if col_cnt - 1 >= 0:
                    area -= min(height, grid[row_cnt][col_cnt - 1])
                if col_cnt + 1 < row_size:
                    area -= min(height, grid[row_cnt][col_cnt + 1])

                result += area
        return result
