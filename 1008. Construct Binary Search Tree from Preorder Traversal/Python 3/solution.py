# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder.pop(0))

        while preorder:
            cur_val = preorder.pop(0)
            node = TreeNode(cur_val)
            temp = root
            while temp:
                if cur_val < temp.val:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = node
                        break
                else:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = node
                        break
        return root
