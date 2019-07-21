class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        result = 0
        cnter = collections.Counter()
        for domino in dominoes:

            cnter[(min(domino), max(domino))] += 1

        for key in cnter:
            freq = cnter[key]
            result += freq * (freq - 1) // 2

        return result
