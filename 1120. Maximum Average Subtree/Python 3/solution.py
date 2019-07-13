# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        max_value, _, _ = self.helper(root)

        return max_value

    def helper(self, root):
        if not root.left and not root.right:
            return root.val, 1, root.val
        total = root.val
        nums = 1
        max_value = 0
        if root.left:
            left_max, left_nums, left_mean = self.helper(root.left)
            nums += left_nums
            total += left_nums * left_mean
            max_value = max(max_value, left_max)

        if root.right:
            right_max, right_nums, right_mean = self.helper(root.right)
            nums += right_nums
            total += right_nums * right_mean
            max_value = max(max_value, right_max)

        mean = total / nums
        # print(root.val, mean)
        max_value = max(max_value, mean)

        return max_value, nums, mean
