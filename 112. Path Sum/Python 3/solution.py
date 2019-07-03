# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = collections.deque()

        stack.append((root, root.val))

        while stack:
            node, pathsum = stack.pop()
            if not node.left and not node.right:
                if pathsum == sum:
                    return True
                else:
                    continue
            if node.left:
                stack.append((node.left, pathsum + node.left.val))
            if node.right:
                stack.append((node.right, pathsum + node.right.val))

        return False
