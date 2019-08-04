class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        size = len(nums)

        odd_temp, even_temp = 0, 0
        for cnt in range(size):
            left_num, right_num = 0, 0
            if cnt - 1 >= 0:
                left_num = nums[cnt - 1]
            if cnt + 1 < size:
                right_num = nums[cnt + 1]
            target = nums[cnt]
            if left_num:
                target = min(left_num - 1, target)
            if right_num:
                target = min(right_num - 1, target)

            if cnt % 2 == 1:
                odd_temp += nums[cnt] - target
            else:
                even_temp += nums[cnt] - target

        result = min(odd_temp, even_temp)
        return result
