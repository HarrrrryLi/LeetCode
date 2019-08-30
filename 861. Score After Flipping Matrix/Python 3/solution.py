class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        result = 0
        row_size, col_size = len(A), len(A[0])

        for row in range(row_size):
            if A[row][0] == 0:
                self.toggleRow(A, row)

        for idx, col in enumerate(zip(*A)):
            zero_count = col.count(0)
            if zero_count > row_size - zero_count:
                self.toggleCol(A, idx)

        return self.calculate_score(A)

    def toggleRow(self, A, row):
        col_size = len(A[0])
        for col in range(col_size):
            A[row][col] = 1 - A[row][col]

    def toggleCol(self, A, col):
        row_size = len(A)
        for row in range(row_size):
            A[row][col] = 1 - A[row][col]

    def binlist2int(self, l):
        result = 0
        for num in l:
            result *= 2
            result += num

        return result

    def calculate_score(self, A):
        result = 0
        for row in A:
            result += self.binlist2int(row)
        return result
