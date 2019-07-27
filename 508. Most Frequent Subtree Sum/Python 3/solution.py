# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        freq = collections.Counter()
        self.helper(root, freq)
        max_freq = max(freq.values())
        result = []
        for key in freq:
            if freq[key] == max_freq:
                result.append(key)
        return result

    def helper(self, root, freq):
        if not root:
            return 0

        _sum = root.val
        if root.left:
            _sum += self.helper(root.left, freq)
        if root.right:
            _sum += self.helper(root.right, freq)

        freq[_sum] += 1

        return _sum
