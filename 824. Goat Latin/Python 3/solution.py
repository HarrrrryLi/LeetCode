class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        result = []
        for idx, word in enumerate(words):
            if word[0].lower() in 'aeiou':
                temp = word + 'ma'
            else:
                temp = word[1:] + word[0] + 'ma'
            temp += 'a' * (idx + 1)
            result.append(temp)

        return ' '.join(result)
