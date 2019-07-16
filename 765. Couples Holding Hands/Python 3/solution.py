class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = {}
        for idx, p in enumerate(row):
            d[p] = idx
        size = len(row)
        result = 0
        for cnt in range(0, size - 2, 2):
            cur = row[cnt]
            if cur % 2 == 0:
                if row[cnt + 1] != cur + 1:
                    result += 1
                    idx = d[cur + 1]
                    row[cnt + 1], row[idx] = cur + 1, row[cnt + 1]
                    d[cur + 1], d[row[idx]] = cnt + 1, idx
            else:
                if row[cnt + 1] != cur - 1:
                    result += 1
                    idx = d[cur - 1]
                    row[cnt + 1], row[idx] = cur - 1, row[cnt + 1]
                    d[cur - 1], d[row[idx]] = cnt + 1, idx
            # print(row)

        return result
