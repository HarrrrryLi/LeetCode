class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size = len(nums2)
        record = {}
        result = []
        stack = collections.deque()
        for idx in range(size - 1, -1, -1):
            num = nums2[idx]
            while stack and nums2[idx] >= stack[-1]:
                stack.pop()
            if stack and num not in record:
                record[num] = stack[-1]

            stack.append(num)

        for num in nums1:
            result.append(record.get(num, -1))

        return result
