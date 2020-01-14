class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        s = str(n)
        start = 1

        for idx, c in enumerate(s):
            if c == '0':
                if idx + 1 < len(s):
                    start = int(s[idx + 1:]) + 1
                else:
                    start = 1
                break
        else:
            if s[-1] == '1':
                start = 2

        for num in range(start, n // 2 + 1):
            if '0' not in str(num) and '0' not in str(n - num):
                return [num, n - num]
