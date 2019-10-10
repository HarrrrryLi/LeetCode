class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        J_set = set(c for c in J)
        for s in S:
            if s in J_set:
                result += 1

        return result
