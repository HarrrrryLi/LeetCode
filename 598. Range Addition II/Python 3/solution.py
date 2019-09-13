class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row, col = m, n

        for r, c in ops:
            row = min(row, r)
            col = min(col, c)

        return row * col
