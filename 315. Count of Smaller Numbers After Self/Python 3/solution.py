# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:

#         size = len(nums)
#         temp = []
#         result = []
#         for idx in range(size - 1, -1, -1):
#             num = nums[idx]
#             idx = bisect.bisect_left(temp, num)
#             result.insert(0, idx)
#             temp.insert(idx, num)

#         return result
#


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        temp = []
        result = 0

        for num in nums:
            idx = bisect.bisect_right(temp, 2 * num)
            result += len(temp) - idx
            bisect.insort(temp, num)

        return result
