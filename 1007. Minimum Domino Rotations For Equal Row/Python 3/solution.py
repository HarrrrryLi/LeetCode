class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        size = len(A)
        candidates = set()
        candidates.add(A[0])
        candidates.add(B[0])

        for cnt in range(size):
            temp = set([A[cnt], B[cnt]])
            candidates &= temp
            if len(candidates) == 0:
                return - 1
        ACnter = collections.Counter(A)
        BCnter = collections.Counter(B)
        result = size

        for num in candidates:
            result = min(result, size - ACnter[num], size - BCnter[num])

        return result
