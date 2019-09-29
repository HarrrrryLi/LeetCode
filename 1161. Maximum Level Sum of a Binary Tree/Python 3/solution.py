# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = collections.defaultdict(int)

        queue = collections.deque()
        queue.append((root, 1))

        while queue:
            node, level = queue.popleft()
            levels[level] += node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        max_level, max_value = 0, float('-inf')

        for key in levels:
            if levels[key] > max_value:
                max_level = key
                max_value = levels[key]
            elif levels[key] == max_value:
                max_level = min(max_level, key)

        return max_level
