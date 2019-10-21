class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        size = len(bulbs)
        days = [0] * size
        for day, position in enumerate(bulbs):
            days[position - 1] = day + 1

        result = float('inf')
        left, right = 0, K + 1

        while right < size:
            for idx in range(left + 1, right):
                if days[idx] < days[left] or days[idx] < days[right]:
                    left, right = idx, idx + K + 1
                    break
            else:
                result = min(result, max(days[left], days[right]))
                left, right = right, right + K + 1

        if result == float('inf'):
            return -1

        return result
