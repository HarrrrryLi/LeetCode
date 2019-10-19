class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        low, high = 0, sum(sweetness) // (K + 1)

        while low < high:
            mid = (low + high + 1) // 2
            if self.check(sweetness, mid, K + 1):
                low = mid
            else:
                high = mid - 1

        return low

    def check(self, sweetness, target, K):
        count = 0
        current = 0
        for sweet in sweetness:
            current += sweet
            if current >= target:
                count += 1
                current = 0

        return count >= K
