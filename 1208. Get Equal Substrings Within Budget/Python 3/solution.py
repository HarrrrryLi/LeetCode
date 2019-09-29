class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = []
        size = len(s)

        for c1, c2 in zip(s, t):
            diff = abs(ord(c1) - ord(c2))
            costs.append(diff)

        left, right = 0, 1
        _sum = costs[0]
        result = 0
        while left <= size - 1:
            if _sum <= maxCost:
                result = max(result, right - left)
            if right == size:
                _sum -= costs[left]
                left += 1
            elif left == right:
                _sum += costs[right]
                right += 1
            elif _sum <= maxCost:
                _sum += costs[right]
                right += 1
            elif _sum > maxCost:
                _sum -= costs[left]
                left += 1

        return result
