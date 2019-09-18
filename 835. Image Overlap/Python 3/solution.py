class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        src, target = [], set()
        row_size, col_size = len(A), len(A[0])

        for row in range(row_size):
            for col in range(col_size):
                if A[row][col]:
                    src.append((row, col))
                if B[row][col]:
                    target.add((row, col))

        result = 0
        for row in range(-row_size + 1, row_size):
            for col in range(-col_size + 1, col_size):
                temp = 0
                for r, c in src:
                    nxtr, nxtc = r + row, c + col
                    if (nxtr, nxtc) in target:
                        temp += 1
                result = max(result, temp)

        return result
