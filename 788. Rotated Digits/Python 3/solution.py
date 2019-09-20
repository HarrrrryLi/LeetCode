class Solution:
    def rotatedDigits(self, N: int) -> int:
        candidates = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}
        result = 0
        for num in range(1, N + 1):
            changed = False
            while num:
                digit = num % 10
                if digit not in candidates:
                    break
                elif candidates[digit] != digit:
                    changed = True
                num //= 10
            else:
                if changed:
                    result += 1

        return result
