class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        result = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            result += right - left + 1
        return result
