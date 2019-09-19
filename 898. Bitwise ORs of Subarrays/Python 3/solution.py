class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        result = set()
        cur = {0}
        for num in A:
            cur = {num | pre for pre in cur} | {num}
            result |= cur
        return len(result)
