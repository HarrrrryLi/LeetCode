class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        col_size = len(colsum)

        row0 = [0] * col_size
        row1 = [0] * col_size

        for idx, s in enumerate(colsum):
            if s == 2:
                if upper and lower:
                    row0[idx] = 1
                    row1[idx] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []

        for idx, s in enumerate(colsum):
            if s == 1:
                if upper:
                    row0[idx] = 1
                    upper -= 1
                elif lower:
                    row1[idx] = 1
                    lower -= 1
                else:
                    return []
        if upper or lower:
            return []

        return [row0, row1]
