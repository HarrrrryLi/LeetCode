class TreeNode:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.value = 0


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        root = self.__buildSegmentTree(arr, 0, len(arr) - 1)
        result = []
        for start, end in queries:
            result.append(self.__querySegmentTree(root, start, end))

        return result

    def __buildSegmentTree(self, arr, start, end):
        root = TreeNode(start, end)
        if start == end:
            root.value = arr[start]
            return root
        mid = (start + end) // 2
        root.left = self.__buildSegmentTree(arr, start, mid)
        root.right = self.__buildSegmentTree(arr, mid + 1, end)
        root.value = root.left.value ^ root.right.value
        return root

    def __querySegmentTree(self, root, qstart, qend):
        if qstart == root.start and qend == root.end:
            return root.value

        mid = (root.start + root.end) // 2
        if mid >= qend:
            return self.__querySegmentTree(root.left, qstart, qend)
        if mid < qstart:
            return self.__querySegmentTree(root.right, qstart, qend)

        return self.__querySegmentTree(root.left, qstart, mid) ^ self.__querySegmentTree(root.right, mid + 1, qend)
