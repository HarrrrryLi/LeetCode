import collections


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = collections.Counter(nums1)

        result = []

        for num in nums2:
            if d[num]:
                result.append(num)
                d[num] -= 1

        return result
