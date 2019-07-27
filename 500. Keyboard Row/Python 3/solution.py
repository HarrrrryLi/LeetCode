class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
                {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
                {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]

        result = []

        for word in words:
            for row in rows:
                if word[0].lower() in row:
                    candidate = row
                    break
            for c in word:
                if c.lower() not in candidate:
                    break
            else:
                result.append(word)

        return result
