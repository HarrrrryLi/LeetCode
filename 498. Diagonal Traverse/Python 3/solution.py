class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        # direction = [(-1, 1), (1, -1)]
        row_size, col_size = len(matrix), len(matrix[0])
        current = (0, 0)
        result = []

        direct = (-1, 1)

        while current != (row_size - 1, col_size - 1):
            row, col = current
            result.append(matrix[row][col])

            nxtr, nxtc = row + direct[0], col + direct[1]

            if nxtr < 0 or nxtr >= row_size or nxtc < 0 or nxtc >= col_size:
                direct = (-direct[0], -direct[1])

            if nxtr < 0:
                nxtr = 0
            elif nxtr >= row_size:
                nxtr = row_size - 1
                nxtc = col + 1

            if nxtc < 0:
                nxtc = 0
            elif nxtc >= col_size:
                nxtc = col_size - 1
                nxtr = row + 1

            current = (nxtr, nxtc)

        result.append(matrix[-1][-1])

        return result
