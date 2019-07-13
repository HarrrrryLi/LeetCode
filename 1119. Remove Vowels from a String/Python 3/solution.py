class Solution:
    def removeVowels(self, S: str) -> str:
        result = []
        for c in S:
            if c not in 'aeiou':
                result.append(c)

        return ''.join(result)
