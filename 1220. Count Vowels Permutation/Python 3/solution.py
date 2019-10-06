class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {'a': 'e', 'e': 'ai', 'i': 'aeou', 'o': 'iu', 'u': 'a'}
        dp = dict()
        for c in 'aeiou':
            dp[c] = 1
        cur = 1

        while cur < n:
            nxt = collections.Counter()
            for c in dp:
                rule = rules[c]
                for nxtc in rule:
                    nxt[nxtc] += dp[c]
            dp = nxt
            cur += 1

        return sum(dp.values()) % (10 ** 9 + 7)
