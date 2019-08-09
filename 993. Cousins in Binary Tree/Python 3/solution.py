# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = collections.deque()
        stack.append((root, 0, None))
        record = []
        while stack:
            node, depth, parent = stack.pop()
            if node.val == x or node.val == y:
                record.append((depth, parent))
            if len(record) == 2:
                break
            if node.left:
                stack.append((node.left, depth + 1, node))
            if node.right:
                stack.append((node.right, depth + 1, node))

        return record[0][0] == record[1][0] and record[0][1] != record[1][1]
