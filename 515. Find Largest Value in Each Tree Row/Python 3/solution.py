# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        record = {}
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            node, depth = queue.popleft()
            if depth not in record:
                record[depth] = node.val
            else:
                record[depth] = max(record[depth], node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        result = []
        for cnt in range(len(record)):
            result.append(record[cnt])
        return result
