class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        result = 0
        temp = 1

        for cnt in range(1, size):
            if nums[cnt] > nums[cnt - 1]:
                temp += 1
            else:
                result = max(result, temp)
                temp = 1

        result = max(result, temp)
        return result
