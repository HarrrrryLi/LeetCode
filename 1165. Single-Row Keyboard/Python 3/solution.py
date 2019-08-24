class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        letter2idx = {c: idx for idx, c in enumerate(keyboard)}

        pre = 0
        result = 0
        for c in word:
            result += abs(letter2idx[c] - pre)
            pre = letter2idx[c]

        return result
