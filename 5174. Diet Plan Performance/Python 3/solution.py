class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        _sum = 0
        result = 0
        size = len(calories)
        for idx in range(k):
            _sum += calories[idx]

        right = k
        while right <= size:
            if _sum < lower:
                result -= 1
            elif _sum > upper:
                result += 1
            if right == size:
                break
            _sum += calories[right]
            _sum -= calories[right - k]
            right += 1

        return result
