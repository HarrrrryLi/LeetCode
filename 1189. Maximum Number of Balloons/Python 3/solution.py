class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnter = collections.Counter(text)
        result = float('inf')
        for c in 'balon':
            if c not in cnter:
                return 0
            if c in 'lo':
                result = min(cnter[c] // 2, result)
            else:
                result = min(cnter[c], result)

        if result == float('inf'):
            return 0
        return result
