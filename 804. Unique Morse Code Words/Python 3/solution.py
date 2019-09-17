class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morses = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                  "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        result = set()

        for word in words:
            temp = ''
            for c in word:
                idx = ord(c) - ord('a')
                temp += morses[idx]
            result.add(temp)

        return len(result)
