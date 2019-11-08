class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        record = {}

        return self.helper(nums, record, True) >= 0

    def helper(self, nums, record, isPlayer1):
        if len(nums) == 1:
            return nums[0] if isPlayer1 else -nums[0]

        key = tuple(nums)
        if key in record:
            return record[key]

        temp1 = list(nums)
        temp2 = list(nums)

        value1 = temp1.pop(0) if isPlayer1 else -temp1.pop(0)
        value2 = temp2.pop() if isPlayer1 else -temp2.pop()

        condition1 = self.helper(temp1, record, not isPlayer1) + value1
        condition2 = self.helper(temp2, record, not isPlayer1) + value2

        if isPlayer1:
            result = max(condition1, condition2)
        else:
            result = min(condition1, condition2)

        record[key] = result
        return result
