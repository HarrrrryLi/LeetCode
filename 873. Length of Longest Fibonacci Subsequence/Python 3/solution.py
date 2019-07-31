class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        Aset = set(A)
        result = 0
        for num1, num2 in itertools.combinations(A, 2):
            num3 = num1 + num2
            if num3 not in Aset:
                continue
            temp = 2
            while num3 in Aset:
                temp += 1
                num1, num2 = num2, num3
                num3 = num1 + num2

            result = max(result, temp)

        return result
