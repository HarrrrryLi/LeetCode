class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row_size, col_size = len(A), len(A[0])
        result = [[0] * row_size for _ in range(col_size)]
        for row_cnt in range(row_size):
            for col_cnt in range(col_size):
                result[col_cnt][row_cnt] = A[row_cnt][col_cnt]

        return result
