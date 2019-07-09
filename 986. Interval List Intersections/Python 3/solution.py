class Solution:
    def intervalIntersection(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        A_size, B_size = len(A), len(B)
        cntA, cntB = 0, 0
        result = []

        while cntA < A_size and cntB < B_size:
            left = max(A[cntA][0], B[cntB][0])
            right = min(A[cntA][1], B[cntB][1])
            if left <= right:
                result.append((left, right))
            if A[cntA][1] < B[cntB][1]:
                cntA += 1
            else:
                cntB += 1

        return result
