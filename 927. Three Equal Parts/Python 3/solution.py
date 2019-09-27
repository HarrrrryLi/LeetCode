class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        size = len(A)
        dp = [0] * size
        dp[0] = A[0]

        for cnt in range(1, size):
            dp[cnt] = dp[cnt - 1] << 1 | A[cnt]

        left, right = 0, size - 1
        while left + 1 < right:
            num1 = dp[left]
            num2 = dp[right - 1] - (dp[left] << (right - 1 - left))
            num3 = dp[-1] - (dp[right - 1] << (size - right))
            if num1 == num2 and num1 == num3:
                return [left, right]
            elif num1 < num3:
                left += 1
            else:
                right -= 1

        return [-1, -1]
