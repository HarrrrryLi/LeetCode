class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if sum((p + mid - 1) // mid for p in piles) > H:
                l = mid + 1
            else:
                r = mid
        return l
