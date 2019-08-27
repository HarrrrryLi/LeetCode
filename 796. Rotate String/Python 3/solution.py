class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        sizeA, sizeB = len(A), len(B)
        if sizeA != sizeB:
            return False

        temp = B * 2

        for idx in range(sizeB):
            if B[idx] == A[0]:
                if temp[idx: sizeB + idx] == A:
                    return True

        return False
