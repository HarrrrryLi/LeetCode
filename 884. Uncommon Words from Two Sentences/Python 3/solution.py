class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        wordsA, wordsB = A.split(' '), B.split(' ')
        recordA, recordB = collections.Counter(
            wordsA), collections.Counter(wordsB)

        result = []
        for key in recordA:
            if key and recordA[key] == 1 and key not in recordB:
                result.append(key)

        for key in recordB:
            if key and recordB[key] == 1 and key not in recordA:
                result.append(key)

        return result
