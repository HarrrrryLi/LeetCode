class Node:
    def __init__(self, start, end, height):
        self.start = start
        self.end = end
        self.height = height
        self.whole = True

        self.left = None
        self.right = None


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        start, end = float('inf'), 0
        for s, e, _ in buildings:
            start = min(start, s)
            end = max(end, e)

        root = Node(start, end, 0)
        for s, e, h in buildings:
            self.update(root, s, e - 1, h)

        result = []
        self.collect(root, result)
        return result

    def create_childern(self, root):
        mid = (root.start + root.end) // 2
        root.left = Node(root.start, mid, root.height)
        root.right = Node(mid + 1, root.end, root.height)

    def update(self, root, start, end, height):
        if root.start >= start and root.end <= end and root.height <= height:
            root.whole = True
            root.height = height
            if root.left:
                self.__update(root, start, end, height)

        if root.whole and root.height >= height:
            return

        if not root.left:
            self.create_childern(root)
        root.height = max(root.height, height)
        root.whole = False
        self.__update(root, start, end, height)

    def __update(self, root, start, end, height):
        mid = (root.start + root.end) // 2
        if mid < start:
            self.update(root.right, start, end, height)
        elif mid >= end:
            self.update(root.left, start, end, height)
        else:
            self.update(root.left, start, mid, height)
            self.update(root.right, mid + 1, end, height)

    def collect(self, root, result):
        if root.whole:
            if not result or result[-1][-1] != root.height:
                result.append([root.start, root.height])
        else:
            if root.left:
                self.collect(root.left, result)
            if root.right:
                self.collect(root.right, result)
