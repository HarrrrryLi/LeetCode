# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        stack = collections.deque()
        path = set()
        path.add((root, 0))
        stack.append((root, 0, path))
        leaves = collections.defaultdict(list)
        while stack:
            node, depth, path = stack.pop()
            if not node.left and not node.right:
                leaves[depth].append(path)
                continue
            if node.left:
                temp = set(path)
                temp.add((node.left, depth + 1))
                stack.append((node.left, depth + 1, temp))
            if node.right:
                temp = set(path)
                temp.add((node.right, depth + 1))
                stack.append((node.right, depth + 1, temp))

        max_depth = max(leaves)
        candidates = leaves[max_depth][0]
        for path in leaves[max_depth]:
            candidates &= path

        return max(candidates, key=lambda x: x[1])[0]
