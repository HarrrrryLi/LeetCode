class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [0, 0]
        for idx in range(size):
            num = nums[idx]
            if nums[abs(num) - 1] < 0:
                result[0] = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for idx, num in enumerate(nums):
            if num > 0:
                result[1] = idx + 1
                break

        return result
