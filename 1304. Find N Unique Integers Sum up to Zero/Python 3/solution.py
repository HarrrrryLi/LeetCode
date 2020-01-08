class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2:
            result.append(0)
            n -= 1

        while n:
            result.append(n)
            result.append(-n)
            n -= 2

        return result
