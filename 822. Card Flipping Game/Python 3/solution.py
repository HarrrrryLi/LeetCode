class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        size = len(fronts)

        candidates = set(fronts + backs)

        for cnt in range(size):
            front = fronts[cnt]
            back = backs[cnt]
            if front == back and front in candidates:
                candidates.remove(front)

        if not candidates:
            return 0

        return min(candidates)
