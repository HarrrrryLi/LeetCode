class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        size = len(nums)
        result = [-1] * size
        stack = collections.deque()
        for i in range(size * 2 - 1, -1, -1):
            idx = i % size
            while stack and nums[idx] >= stack[-1]:
                stack.pop()
            if stack and result[idx] == -1:
                result[idx] = stack[-1]

            stack.append(nums[idx])

        return result
