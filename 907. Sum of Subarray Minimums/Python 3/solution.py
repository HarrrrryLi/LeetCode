class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        size = len(A)
        left, right, left_stack, right_stack = [
            0] * size, [0] * size, collections.deque(), collections.deque()

        for idx in range(size):
            count = 1
            while left_stack and left_stack[-1][0] > A[idx]:
                count += left_stack.pop()[1]
            left[idx] = count
            left_stack.append([A[idx], count])

        for idx in range(size - 1, -1, -1):
            count = 1
            while right_stack and right_stack[-1][0] >= A[idx]:
                count += right_stack.pop()[1]
            right[idx] = count
            right_stack.append([A[idx], count])

        return sum(a * l * r for a, l, r in zip(A, left, right)) % (10 ** 9 + 7)
