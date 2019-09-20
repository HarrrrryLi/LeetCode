class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            gd = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if gd <= dist:
                return False
        return True
