class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        TARGET = 5000
        result = 0
        cur = 0

        for weight in arr:
            if cur + weight <= TARGET:
                result += 1
                cur += weight
            else:
                break

        return result
