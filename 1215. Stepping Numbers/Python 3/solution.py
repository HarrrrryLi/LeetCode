class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        dp = list(range(10))
        cnt = 1
        if low < 10:
            start_idx = low
        else:
            start_idx = -1

        while True:
            cur = dp[cnt]
            last_digit = cur % 10
            if last_digit >= 1:
                temp = cur * 10
                temp += last_digit - 1
                if temp <= high:
                    dp.append(temp)
                    if dp[-2] < low and temp >= low:
                        start_idx = len(dp) - 1
                if temp >= high:
                    if start_idx == -1:
                        return []
                    return dp[start_idx:]
            if last_digit < 9:
                temp = cur * 10
                temp += last_digit + 1
                if temp <= high:
                    dp.append(temp)
                    if dp[-2] < low and temp >= low:
                        start_idx = len(dp) - 1
                if temp >= high:
                    if start_idx == -1:
                        return []
                    return dp[start_idx:]

            cnt += 1
