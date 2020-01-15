class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = []
        for idx in range(0, size, 2):
            result += [nums[idx + 1]] * nums[idx]

        return result
