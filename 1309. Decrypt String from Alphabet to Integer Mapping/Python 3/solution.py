class Solution:
    def freqAlphabets(self, s: str) -> str:
        size = len(s)
        idx = 0
        result = []
        while idx < size:
            if idx + 2 < size and s[idx + 2] == '#':
                num = int(s[idx: idx + 2])
                idx += 3
            else:
                num = int(s[idx])
                idx += 1
            c = chr(ord('a') + num - 1)
            result.append(c)

        return ''.join(result)
