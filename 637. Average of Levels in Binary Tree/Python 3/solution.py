# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return 0

        _sum = collections.defaultdict(int)
        _count = collections.Counter()

        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            _sum[level] += node.val
            _count[level] += 1
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        result = [0] * (level + 1)
        for key in _sum:
            result[key] = _sum[key] / _count[key]

        return result
