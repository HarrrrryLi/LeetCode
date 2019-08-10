class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_size, col_size = len(matrix), len(matrix[0])

        for col_cnt in range(col_size):
            row, col = 0, col_cnt
            num = matrix[row][col]
            while row < row_size and col < col_size:
                if matrix[row][col] != num:
                    return False
                row += 1
                col += 1

        for row_cnt in range(1, row_size):
            row, col = row_cnt, 0
            num = matrix[row][col]
            while row < row_size and col < col_size:
                if matrix[row][col] != num:
                    return False
                row += 1
                col += 1

        return True
