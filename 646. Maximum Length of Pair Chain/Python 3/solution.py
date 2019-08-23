class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        size = len(pairs)
        dp = [1] * size
        pairs.sort(key=lambda x: (x[1], x[0]))
        end = [x[1] for x in pairs]

        for idx, pair in enumerate(pairs):
            i = bisect.bisect_left(end, pair[0])
            if i > 0:
                dp[idx] = max(dp[:i]) + 1

        return max(dp)
