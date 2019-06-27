class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digits = []
        letters = []
        letter_dict = {}
        for log in logs:
            words = log.split(' ')
            if words[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                letter_dict[log] = ' '.join(words[1:])

        letters.sort(key=lambda x: (letter_dict[x], x))
        letters.extend(digits)

        return letters
