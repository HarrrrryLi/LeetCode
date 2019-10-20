class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        longest_time = max(endTime)
        dp = [0] * (longest_time + 1)
        current_max = 0
        pre = 0
        info = sorted(zip(startTime, endTime, profit))

        for start, end, pro in info:
            for idx in range(pre, start + 1):
                current_max = max(current_max, dp[idx])

            pre = start
            dp[end] = max(dp[end], current_max + pro)

        for idx in range(start, longest_time + 1):
            current_max = max(current_max, dp[idx])

        return current_max
