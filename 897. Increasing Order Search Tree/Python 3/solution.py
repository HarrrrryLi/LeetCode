# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = self.inorder(root)
        print(l)
        size = len(l)
        result = l[0]
        temp = result
        for cnt in range(1, size):
            temp.right = l[cnt]
            temp.left = None
            temp = temp.right

        temp.left = None
        temp.right = None

        return result

    def inorder(self, root):
        if not root:
            return []
        result = []
        if root.left:
            result += self.inorder(root.left)
        result.append(root)
        if root.right:
            result += self.inorder(root.right)

        return result
