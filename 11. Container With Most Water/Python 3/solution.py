class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            left_height, right_height = height[left], height[right]
            result = max(result, min(left_height, right_height) * (right - left))
            if left_height <= right_height:
                left += 1
            else:
                right -= 1

        return result
