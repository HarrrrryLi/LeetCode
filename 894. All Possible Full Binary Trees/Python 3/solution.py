# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def allPossibleFBT(self, N: int) -> list[TreeNode]:
        dp = collections.defaultdict(list)
        return self.helper(N, dp)

    def helper(self, N, dp):
        if N == 1:
            return [TreeNode(0)]

        if N in dp:
            return dp[N]
        result = []
        for cnt in range(1, N - 1, 2):
            for left in self.helper(cnt, dp):
                for right in self.helper(N - 1 - cnt, dp):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result.append(root)

        return result
