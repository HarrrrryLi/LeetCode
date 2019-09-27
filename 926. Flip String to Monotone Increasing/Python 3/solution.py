class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        size = len(S)
        c2idx = collections.defaultdict(list)
        for idx, c in enumerate(S):
            c2idx[c].append(idx)
        
        dp = {True: 0, False: 0}
        if S[0] == '0':
            dp[False] = 1
        else:
            dp[True] = 1

        for cnt in range(1, size):
            nxt = {}
            if S[cnt] == '0':
                nxt[True] = dp[True]
                nxt[False] = min(dp[False], dp[True]) + 1
            else:
                nxt[False] = min(dp[False], dp[True])
                nxt[True] = dp[True] + 1
            dp = nxt

        return min(dp[True], dp[False])
