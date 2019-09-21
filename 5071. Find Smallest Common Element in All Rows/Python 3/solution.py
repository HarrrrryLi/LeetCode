class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        row_size, col_size = len(mat), len(mat[0])
        indices = [0] * row_size

        while True:
            max_value = mat[0][indices[0]]
            for row in range(1, row_size):
                if mat[row][indices[row]] > max_value:
                    max_value = mat[row][indices[row]]
            cnt = 0
            for row in range(row_size):
                if mat[row][indices[row]] == max_value:
                    cnt += 1
                else:
                    indices[row] += 1
                    if indices[row] >= col_size:
                        return -1
            if cnt == row_size:
                return max_value
