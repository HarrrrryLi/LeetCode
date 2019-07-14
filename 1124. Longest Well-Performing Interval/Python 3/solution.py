class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        seen = dict()
        score = 0
        result = 0

        for idx, hour in enumerate(hours):
            if hour > 8:
                score += 1
            else:
                score -= 1

            if score > 0:
                result = idx + 1

            if score not in seen:
                seen[score] = idx

            if score - 1 in seen:
                result = max(result, idx - seen[score - 1])

        return result
