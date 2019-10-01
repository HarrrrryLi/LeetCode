class TreeNode():
    def __init__(self):
        self.range = []
        self.left = None
        self.right = None
        self.sum = 0


class NumArray:
    def __init__(self, nums: List[int]):
        if not nums:
            self.root = None
        else:
            self.root = self.__buildSegTree(nums, 0, len(nums) - 1)

    def __buildSegTree(self, nums, left, right):
        root = TreeNode()
        root.range = [left, right]
        if left < right:
            mid = (left + right) // 2
            root.left = self.__buildSegTree(nums, left, mid)
            root.right = self.__buildSegTree(nums, mid + 1, right)
            root.sum = root.left.sum + root.right.sum
        else:
            root.sum = nums[left]

        return root

    def update(self, i: int, val: int) -> None:
        self.__update(i, val, self.root)

    def __update(self, i, val, root):
        if not root:
            return

        if root.range[0] == i and root.range[1] == i:
            diff = val - root.sum
        else:
            mid = (root.range[0] + root.range[1]) // 2
            if i <= mid:
                diff = self.__update(i, val, root.left)
            else:
                diff = self.__update(i, val, root.right)

        root.sum += diff

        return diff

    def sumRange(self, i: int, j: int) -> int:
        return self.__sumRange(i, j, self.root)

    def __sumRange(self, i, j, root):
        if not root:
            return 0

        if root.range[0] == i and root.range[1] == j:
            return root.sum

        mid = (root.range[0] + root.range[1]) // 2
        if j <= mid:
            return self.__sumRange(i, j, root.left)
        elif i > mid:
            return self.__sumRange(i, j, root.right)
        else:
            return self.__sumRange(i, mid, root.left) + self.__sumRange(mid + 1, j, root.right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
