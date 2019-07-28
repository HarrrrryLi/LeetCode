class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        letters = dict()
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for idx, s in enumerate(board):
            for c in s:
                letters[ord(c)] = idx
        result = ''
        current = ord('a')
        for c in target:
            tc = ord(c)
            if tc == current:
                result += '!'
            elif tc > current:
                while letters[current] != letters[tc]:
                    current += 5
                    if current > ord('z'):
                        result += 'L' * (current - ord('z'))
                        current = ord('z')
                    result += 'D'
                diff = tc - current
                if diff >= 0:
                    result += 'R' * diff
                else:
                    result += 'L' * -diff
                result += '!'
            else:
                while letters[current] != letters[tc]:
                    current -= 5
                    result += 'U'
                diff = tc - current
                if diff >= 0:
                    result += 'R' * diff
                else:
                    result += 'L' * -diff
                result += '!'
            current = tc

        return result
