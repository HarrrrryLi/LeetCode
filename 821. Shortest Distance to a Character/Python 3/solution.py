class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        indexes = []

        for idx, c in enumerate(S):
            if c == C:
                indexes.append(idx)

        result = []

        for idx, c in enumerate(S):
            if c == C:
                result.append(0)
                continue
            i = bisect.bisect(indexes, idx)
            if i == 0:
                result.append(indexes[0] - idx)
            elif i == len(indexes):
                result.append(idx - indexes[-1])
            else:
                result.append(min(idx - indexes[i - 1], indexes[i] - idx))

        return result
