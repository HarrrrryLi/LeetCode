# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = collections.deque()
        stack.append((root, False, False))
        result = 0

        while stack:
            node, even_grand, even_parent = stack.pop()
            if even_grand:
                result += node.val

            even_cur = not node.val % 2
            if node.left:
                stack.append((node.left, even_parent, even_cur))
            if node.right:
                stack.append((node.right, even_parent, even_cur))

        return result
