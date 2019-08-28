class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N)[2:]

        result = 0
        pre = -1

        for idx, c in enumerate(s):
            if c == '1':
                if pre != -1:
                    result = max(idx - pre, result)
                pre = idx

        return result
