class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        q = len(B) // len(A)
        for i in range(3):
            if B in A * (q + i):
                return q + i
        return -1
