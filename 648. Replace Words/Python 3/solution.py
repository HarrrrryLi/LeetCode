class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:

        words = sentence.split(' ')

        for idx, word in enumerate(words):
            for candidate in dict:
                if word.startswith(candidate):
                    words[idx] = candidate
                    break

        return ' '.join(words)
