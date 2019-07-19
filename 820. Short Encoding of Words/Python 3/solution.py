class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        reverse = []

        for word in words:
            reverse.append(word[::-1])
        reverse.sort()

        cnt = 0

        while cnt < len(reverse) - 1:
            word1 = reverse[cnt]
            word2 = reverse[cnt + 1]
            if word2.startswith(word1):
                reverse.pop(cnt)
            else:
                cnt += 1

        result = len(reverse)

        for word in reverse:
            result += len(word)

        return result
