class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        if not mines:
            return N // 2

        result = 0
        rows, cols = collections.defaultdict(
            list), collections.defaultdict(list)
        for row, col in mines:
            idx = bisect.bisect(rows[row], col)
            rows[row].insert(idx, col)
            idx = bisect.bisect(cols[col], row)
            cols[col].insert(idx, row)
        # print(rows)
        result = 0
        for row_cnt in range(N):
            for col_cnt in range(N):
                if row_cnt in rows:
                    idx = bisect.bisect(rows[row_cnt], col_cnt)
                    if idx == 0:
                        left = col_cnt + 1
                        right = rows[row_cnt][idx] - col_cnt
                    elif idx == len(rows[row_cnt]):
                        left = col_cnt - rows[row_cnt][idx - 1]
                        right = N - col_cnt
                    else:
                        left = col_cnt - rows[row_cnt][idx - 1]
                        right = rows[row_cnt][idx] - col_cnt
                else:
                    left = col_cnt + 1
                    right = N - col_cnt
                if col_cnt in cols:
                    idx = bisect.bisect(cols[col_cnt], row_cnt)
                    if idx == 0:
                        up = row_cnt + 1
                        down = cols[col_cnt][idx] - row_cnt
                    elif idx == len(cols[col_cnt]):
                        up = row_cnt - cols[col_cnt][idx - 1]
                        down = N - row_cnt
                    else:
                        up = row_cnt - cols[col_cnt][idx - 1]
                        down = cols[col_cnt][idx] - row_cnt
                else:
                    up = row_cnt + 1
                    down = N - row_cnt

                result = max(result, min(left, right, up, down))

        return result
