class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        result = 0
        max_len = int(math.ceil(math.sqrt(8 * N + 1) + 1 / 2))
        for n in range(1, max_len):
            numerator = 2 * N - n * (n - 1)
            denominator = 2 * n
            if numerator % denominator == 0:
                x = numerator // denominator
                if x > 0 and x <= N:
                    result += 1
        return result
