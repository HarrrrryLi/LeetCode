class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = sum(A) - sum(B)
        setB = set(B)

        for num in A:
            if num - diff // 2 in setB:
                return [num, num - diff // 2]
