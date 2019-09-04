class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_cnt = 0
        o_cnt = 0

        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    x_cnt += 1
                elif board[row][col] == 'O':
                    o_cnt += 1

        if o_cnt > x_cnt or x_cnt >= o_cnt + 2:
            return False

        success = []
        for row in board:
            cur = row[0]
            if cur == ' ':
                continue
            for col in range(1, 3):
                if row[col] != cur:
                    break
            else:
                success.append((cur, 'r'))
        for col in range(3):
            cur = board[0][col]
            if cur == ' ':
                continue
            for row in range(1, 3):
                if board[row][col] != cur:
                    break
            else:
                success.append((cur, 'c'))
        if board[0][0] != ' ' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            success.append((board[1][1], 'd'))
        if board[0][2] != ' ' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            success.append((board[1][1], 'd'))

        if len(success) < 1:
            return True
        if len(success) == 1:
            if success[0][0] == 'X' and x_cnt == o_cnt:
                return False
            if success[0][0] == 'O' and x_cnt == o_cnt + 1:
                return False
            return True
        if len(success) == 2:
            if success[0][1] == 'd' and success[1][1] == 'd':
                return True
            elif success[0][0] == success[1][0] and success[0][1] != success[1][1]:
                return True

        return False
