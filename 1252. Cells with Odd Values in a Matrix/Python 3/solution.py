class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0] * m for _ in range(n)]
        for row, col in indices:
            for r in range(n):
                matrix[r][col] += 1
            for c in range(m):
                matrix[row][c] += 1

        result = 0

        for row in range(n):
            for col in range(m):
                if matrix[row][col] % 2:
                    result += 1

        return result
