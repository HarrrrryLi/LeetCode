class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        result = []
        size = len(s)
        dp = []
        dp.append([0] * 26)
        dp[0][ord(s[0]) - ord('a')] = 1

        for idx in range(1, size):
            dp.append(list(dp[idx - 1]))
            dp[idx][ord(s[idx]) - ord('a')] += 1

        for left, right, k in queries:
            odd_nums = 0
            if left == 0:
                for idx in range(26):
                    if dp[right][idx] % 2 == 1:
                        odd_nums += 1
            else:
                for idx in range(26):
                    if (dp[right][idx] - dp[left - 1][idx]) % 2 == 1:
                        odd_nums += 1

            if odd_nums > 1 and odd_nums // 2 > k:
                result.append(False)
            else:
                result.append(True)

        return result
