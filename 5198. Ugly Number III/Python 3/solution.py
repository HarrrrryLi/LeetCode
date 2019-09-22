class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        candidates = [a, b, c]
        delta = [a, b, c]
        result = 0

        cnt = 0
        while cnt < n:
            min_value = min(candidates)
            min_idx = []
            min2nd = float('inf')
            result = min_value
            min_cnt = 0
            for idx in range(3):
                if candidates[idx] == min_value:
                    min_cnt += 1
                    min_idx.append(idx)
                else:
                    min2nd = min(min2nd, candidates[idx])
            if min2nd != float('inf') and min_cnt == 1:
                idx = min_idx[0]
                addnum = max(
                    1, min(n - cnt, (min2nd - min_value + delta[idx] - 1) // delta[idx]))
                candidates[idx] += addnum * delta[idx]
                cnt += addnum
                result = candidates[idx] - delta[idx]
            else:
                for idx in min_idx:
                    candidates[idx] += delta[idx]
                cnt += 1
        return result
