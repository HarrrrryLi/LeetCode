# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1, tree2 = self.tree2list(root1), self.tree2list(root2)
        result = []
        size1, size2 = len(tree1), len(tree2)
        ptr1, ptr2 = 0, 0

        while ptr1 < size1 and ptr2 < size2:
            if tree1[ptr1] <= tree2[ptr2]:
                result.append(tree1[ptr1])
                ptr1 += 1
            else:
                result.append(tree2[ptr2])
                ptr2 += 1

        if ptr1 == size1:
            for cnt in range(ptr2, size2):
                result.append(tree2[cnt])
        else:
            for cnt in range(ptr1, size1):
                result.append(tree1[cnt])

        return result

    def tree2list(self, root):
        result = []
        if not root:
            return result

        if root.left:
            result = self.tree2list(root.left)

        result += [root.val]

        if root.right:
            result += self.tree2list(root.right)

        return result
