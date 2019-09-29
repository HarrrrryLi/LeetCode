class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        Cnter = collections.Counter(chars)
        result = 0
        for word in words:
            cnter = collections.Counter(word)
            for key in cnter:
                if cnter[key] > Cnter[key]:
                    break
            else:
                result += len(word)

        return result
