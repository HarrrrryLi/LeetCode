class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letterPool = collections.Counter(letters)
        result = 0

        return self.helper(words, 0, letterPool, score)

    def helper(self, words, start, letterPool, score):
        result = 0
        size = len(words)

        for idx in range(start, size):
            word = words[idx]
            needed = collections.Counter(word)
            temp = collections.Counter(letterPool)
            s = 0
            for key in needed:
                if needed[key] <= temp[key]:
                    temp[key] -= needed[key]
                    s += needed[key] * score[ord(key) - ord('a')]
                else:
                    break
            else:
                s += self.helper(words, idx + 1, temp, score)
                result = max(s, result)

        return result
