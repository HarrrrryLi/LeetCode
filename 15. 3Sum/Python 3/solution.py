class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        size = len(nums)
        idx = 0
        while idx < size:
            num = nums[idx]
            left, right = idx + 1, size - 1

            while left < right:
                _sum = num + nums[left] + nums[right]
                if _sum == 0:
                    result.append([num, nums[left], nums[right]])
                    left = self.move2right(nums, left, right)
                elif _sum < 0:
                    left = self.move2right(nums, left, right)
                else:
                    right = self.move2left(nums, left, right)

            idx = self.move2right(nums, idx, size)

        return result

    def move2right(self, nums, left, right):
        left += 1
        while left < right and nums[left] == nums[left - 1]:
            left += 1
        return left

    def move2left(self, nums, left, right):
        right -= 1
        while left < right and nums[right] == nums[right + 1]:
            right -= 1

        return right
