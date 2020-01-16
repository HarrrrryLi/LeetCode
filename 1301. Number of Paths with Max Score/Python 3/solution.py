class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        row_size, col_size = len(board), len(board[0])
        dp = [[(0, 0)] * col_size for _ in range(row_size)]
        dp[-1][-1] = (0, 1)

        for row_cnt in range(row_size - 1, -1, -1):
            for col_cnt in range(col_size - 1, -1, -1):
                if board[row_cnt][col_cnt] == 'X':
                    continue

                cur_sum, cur_num = dp[row_cnt][col_cnt]
                num = int(board[row_cnt][col_cnt]
                          ) if board[row_cnt][col_cnt].isdigit() else 0

                if row_cnt + 1 < row_size and board[row_cnt + 1][col_cnt] != 'X':
                    bot_sum, bot_num = dp[row_cnt + 1][col_cnt]
                    bot_sum += num
                    cur_sum, cur_num = self.update(
                        cur_sum, cur_num, bot_sum, bot_num)

                if col_cnt + 1 < col_size and board[row_cnt][col_cnt + 1] != 'X':
                    right_sum, right_num = dp[row_cnt][col_cnt + 1]
                    right_sum += num
                    cur_sum, cur_num = self.update(
                        cur_sum, cur_num, right_sum, right_num)

                if row_cnt + 1 < row_size and col_cnt + 1 < col_size and board[row_cnt + 1][col_cnt + 1] != 'X':
                    bot_right_sum, bot_right_num = dp[row_cnt + 1][col_cnt + 1]
                    bot_right_sum += num
                    cur_sum, cur_num = self.update(
                        cur_sum, cur_num, bot_right_sum, bot_right_num)

                dp[row_cnt][col_cnt] = (cur_sum, cur_num)

        max_sum, num = dp[0][0]
        if not num:
            return [0, 0]

        return [max_sum, num % (10 ** 9 + 7)]

    def update(self, cur_sum, cur_num, _sum, num):
        if _sum > cur_sum:
            cur_sum = _sum
            cur_num = num
        elif _sum == cur_sum:
            cur_num += num

        return cur_sum, cur_num
