class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = 0

        sorted_nums = sorted(nums)

        for idx, num in enumerate(nums):
            new_idx = bisect.bisect_left(sorted_nums, num)
            sorted_nums.pop(new_idx)
            i = bisect.bisect_left(sorted_nums, (num + 1) // 2)
            result += i

        return result
