class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        size = len(A)
        A.sort()

        pow2 = [1]
        for _ in range(1, size):
            pow2.append(pow2[-1] * 2)

        result = 0
        for idx, num in enumerate(A):
            result = result + (pow2[idx] - pow2[size - 1 - idx]) * num
        return result % (10 ** 9 + 7)
