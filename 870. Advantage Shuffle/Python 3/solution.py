class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        size = len(A)
        A.sort()
        result = [-1] * size
        sorted_B = sorted(enumerate(B), key=lambda x: x[1], reverse=True)

        for idx, num in sorted_B:
            if num >= A[-1]:
                result[idx] = A.pop(0)
            else:
                result[idx] = A.pop()

        return result
