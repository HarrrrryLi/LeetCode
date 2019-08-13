# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque()
        queue.append((root, 0))
        result_node = root.val
        result_depth = 0

        while queue:
            node, depth = queue.popleft()
            if not node.left:
                if depth > result_depth:
                    result_node = node.val
                    result_depth = depth
            else:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return result_node
