class Solution:
    def subarraysDivByK(self, A: list[int], K: int) -> int:

        _sum = 0
        mods = [0] * K
        result = 0
        mods[0] = 1

        for ele in A:
            _sum += ele
            remain = _sum % K
            result += mods[remain]
            mods[remain] += 1

        return result
