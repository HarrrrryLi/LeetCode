# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        record = collections.defaultdict(int)

        stack = collections.deque()
        stack.append((root, 0))

        while stack:
            node, depth = stack.pop()
            record[depth] += node.val

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        deepest = max(record.keys())
        return record[deepest]
