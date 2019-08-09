class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        size = len(A)
        curr = 0
        dp = [0] * size
        for i in range(size):
            if i >= K:

                p = curr - dp[i - K]
            else:
                p = curr

            if ((p % 2 == 0 and A[i] == 0) or (p % 2 == 1 and A[i] == 1)):
                if i > size - K:
                    return -1
                curr = curr + 1
            dp[i] = curr
        return curr
