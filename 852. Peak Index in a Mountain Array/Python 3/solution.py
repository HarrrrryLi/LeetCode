class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        size = len(A)
        for idx, num in enumerate(A):
            if idx + 1 < size and num >= A[idx + 1]:
                return idx

        return size - 1
