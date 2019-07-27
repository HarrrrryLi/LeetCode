class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        size = len(Capital)
        params = [(Capital[idx], Profits[idx]) for idx in range(size)]
        params.sort(key=lambda x: (-x[1], x[0]))

        while k and params:
            max_profit = 0
            max_idx = -1
            for i, (c, p) in enumerate(params):
                if c <= W:
                    max_profit = p
                    max_idx = i
                    break

            W += max_profit
            params.pop(max_idx)
            k -= 1

        return W
