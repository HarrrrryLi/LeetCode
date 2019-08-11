class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        record = {}
        result = self.helper(d, f, target, record)

        return result % (10 ** 9 + 7)

    def helper(self, d, f, target, record):
        if not target:
            return 0
        if d == 1:
            if target <= f:
                return 1
            else:
                return 0
        result = 0

        if (d, target) in record:
            return record[(d, target)]
        for num in range(1, f + 1):
            if num <= target:
                result += self.helper(d - 1, f, target - num, record)

        record[(d, target)] = result

        return result
