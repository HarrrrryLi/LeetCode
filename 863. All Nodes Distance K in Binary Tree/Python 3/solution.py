# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        dist = {}

        queue = collections.deque()
        queue.append((root, [root]))

        while queue:
            cur, path = queue.popleft()
            if cur == target:
                size = len(path)
                for idx in range(size - 1, -1, -1):
                    node = path[idx]
                    dist[node] = size - 1 - idx
                break
            else:
                if cur.left:
                    temp = list(path)
                    temp.append(cur.left)
                    queue.append((cur.left, temp))
                if cur.right:
                    temp = list(path)
                    temp.append(cur.right)
                    queue.append((cur.right, temp))

        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            node = queue.popleft()
            if dist[node] == K:
                result.append(node.val)
            if node.left:
                if node.left not in dist:
                    dist[node.left] = dist[node] + 1
                queue.append(node.left)
            if node.right:
                if node.right not in dist:
                    dist[node.right] = dist[node] + 1
                queue.append(node.right)

        return result
