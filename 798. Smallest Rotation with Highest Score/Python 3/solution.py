class Solution(object):
    def bestRotation(self, A):
        N = len(A)
        dp = [0] * N
        for i, x in enumerate(A):
            left, right = (i - x + 1) % N, (i + 1) % N
            dp[left] -= 1
            dp[right] += 1
            if left > right:
                dp[0] -= 1

        best = -N
        ans = cur = 0
        for i, score in enumerate(dp):
            cur += score
            if cur > best:
                best = cur
                ans = i

        return ans
