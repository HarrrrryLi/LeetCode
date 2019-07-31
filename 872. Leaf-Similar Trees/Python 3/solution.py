# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.DFS(root1) == self.DFS(root2)

    def DFS(self, root):
        if not root:
            return []
        stack = collections.deque()
        result = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                result.append(node.val)
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
