class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row_size, col_size = len(A), len(A[0])
        result = [[0] * col_size for _ in range(row_size)]
        for row_cnt in range(row_size):
            for col_cnt in range(col_size):
                result[row_cnt][col_size - 1 - col_cnt] = 1 - \
                    A[row_cnt][col_cnt]

        return result
