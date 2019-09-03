# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = collections.deque()
        stack.append(root)
        result = 0
        while stack:
            node = stack.pop()
            if node.val >= L and node.val <= R:
                result += node.val
            if node.left and node.val > L:
                stack.append(node.left)

            if node.right and node.val < R:
                stack.append(node.right)

        return result
