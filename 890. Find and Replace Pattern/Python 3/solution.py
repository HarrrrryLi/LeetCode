class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            if self.match(word, pattern):
                result.append(word)
        return result

    def match(self, s, t):
        record = {}
        reverse = set()

        for c1, c2 in zip(s, t):
            if c1 in record and record[c1] != c2:
                return False
            if c1 not in record:
                if c2 in reverse:
                    return False
                record[c1] = c2
                reverse.add(c2)

        return True
