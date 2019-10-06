class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        Cnter = {0: 0, 1: 0}
        for chip in chips:
            Cnter[chip % 2] += 1

        return min(Cnter.values())
