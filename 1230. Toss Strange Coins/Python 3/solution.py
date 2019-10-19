class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = {0: 1}

        for p in prob:
            nxt = {}
            for key in dp:
                nxt[key] = nxt.get(key, 0) + dp[key] * (1 - p)
                if key + 1 <= target:
                    nxt[key + 1] = nxt.get(key + 1, 0) + dp[key] * p
            dp = nxt

        return dp[target]
