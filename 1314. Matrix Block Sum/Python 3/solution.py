class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        row_size, col_size = len(mat), len(mat[0])
        record = [[0] * col_size for _ in range(row_size)]

        record[0][0] = mat[0][0]
        for col in range(1, col_size):
            record[0][col] = mat[0][col] + record[0][col - 1]

        for row in range(1, row_size):
            record[row][0] = mat[row][0] + record[row - 1][0]

        for row in range(1, row_size):
            for col in range(1, col_size):
                record[row][col] = record[row - 1][col] + \
                    record[row][col - 1] - \
                    record[row - 1][col - 1] + mat[row][col]

        result = [[0] * col_size for _ in range(row_size)]

        for row in range(row_size):
            for col in range(col_size):
                cnt = 0
                row_max, row_min = min(
                    row + K, row_size - 1), max(row - K, 0) - 1
                col_max, col_min = min(
                    col + K, col_size - 1), max(col - K, 0) - 1
                result[row][col] = record[row_max][col_max]

                if row_min != -1:
                    result[row][col] -= record[row_min][col_max]
                    cnt += 1
                if col_min != -1:
                    result[row][col] -= record[row_max][col_min]
                    cnt += 1

                if cnt == 2:
                    result[row][col] += record[row_min][col_min]

        return result
