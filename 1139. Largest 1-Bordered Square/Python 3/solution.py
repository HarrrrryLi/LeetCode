class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])
        dp = [[(0, 0)] * col_size for _ in range(row_size)]
        for row in range(row_size - 1, -1, -1):
            for col in range(col_size - 1, -1, -1):
                if grid[row][col] == 0:
                    dp[row][col] = (0, 0)
                else:
                    bot, right = 1, 1
                    if row + 1 < row_size:
                        bot += dp[row + 1][col][0]
                    if col + 1 < col_size:
                        right += dp[row][col + 1][1]
                    dp[row][col] = (bot, right)
        result = 0
        for row in range(row_size):
            for col in range(col_size):
                if not grid[row][col]:
                    continue
                bot, right = dp[row][col]
                edge = min(bot, right)
                for cnt in range(edge, 0, -1):
                    nxt_row = row + cnt - 1
                    nxt_col = col + cnt - 1
                    if nxt_row < row_size and nxt_col < col_size and dp[nxt_row][col][1] >= cnt and dp[row][nxt_col][0] >= cnt:
                        result = max(result, cnt * cnt)
                        break
        return result
