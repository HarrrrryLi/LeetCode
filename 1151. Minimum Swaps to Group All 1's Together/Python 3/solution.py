class Solution:
    def minSwaps(self, data: List[int]) -> int:
        size = len(data)
        nums = data.count(1)
        dp = [0] * (size + 1)
        result = size

        for idx, num in enumerate(data):
            dp[idx + 1] = dp[idx]
            if not num:
                dp[idx + 1] += 1
            if idx + 1 >= nums:
                result = min(result, dp[idx + 1] - dp[idx + 1 - nums])

        return result
