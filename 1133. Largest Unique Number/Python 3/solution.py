class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq = collections.Counter(A)
        result = -1
        for key in freq:
            if freq[key] == 1:
                result = max(result, key)

        return result
