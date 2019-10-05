# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        tree1 = set()
        self.DFS(root1, tree1)
        stack = collections.deque()
        stack.append(root2)

        while stack:
            cur = stack.pop()
            if target - cur.val in tree1:
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return False

    def DFS(self, root, nodes):
        if not root:
            return

        nodes.add(root.val)
        if root.left:
            self.DFS(root.left, nodes)
        if root.right:
            self.DFS(root.right, nodes)
