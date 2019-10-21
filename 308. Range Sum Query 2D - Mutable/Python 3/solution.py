class Node:
    def __init__(self, row_start, row_end, col_start, col_end):
        self.row_start = row_start
        self.row_end = row_end
        self.col_start = col_start
        self.col_end = col_end
        self.sum = 0

        self.left_top = None
        self.left_bottom = None
        self.right_top = None
        self.right_bottom = None


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.root = Node(0, 0, 0, 0)
            return

        row_size, col_size = len(matrix), len(matrix[0])
        self.root = self._init(0, row_size - 1, 0, col_size - 1, matrix)

    def _init(self, row_start, row_end, col_start, col_end, matrix):
        node = Node(row_start, row_end, col_start, col_end)
        if row_start == row_end and col_start == col_end:
            node.sum = matrix[row_start][col_start]
            return node

        row_mid = (row_start + row_end) // 2
        col_mid = (col_start + col_end) // 2

        node.left_top = self._init(
            row_start, row_mid, col_start, col_mid, matrix)
        node.sum += node.left_top.sum
        if col_mid + 1 <= col_end:
            node.right_top = self._init(
                row_start, row_mid, col_mid + 1, col_end, matrix)
            node.sum += node.right_top.sum
        if row_mid + 1 <= row_end:
            node.left_bottom = self._init(
                row_mid + 1, row_end, col_start, col_mid, matrix)
            node.sum += node.left_bottom.sum
            if node.right_top:
                node.right_bottom = self._init(
                    row_mid + 1, row_end, col_mid + 1, col_end, matrix)
                node.sum += node.right_bottom.sum

        return node

    def update(self, row: int, col: int, val: int) -> None:
        self._update(self.root, row, col, val)

    def _update(self, root, row, col, val):
        if root.row_start == root.row_end and root.row_start == row and root.col_start == root.col_end and root.col_start == col:
            diff = val - root.sum
            root.sum = val
            return diff

        row_mid = (root.row_start + root.row_end) // 2
        col_mid = (root.col_start + root.col_end) // 2
        diff = 0

        if row_mid >= row:
            if col_mid >= col:
                diff = self._update(root.left_top, row, col, val)
            else:
                if col_mid + 1 <= root.col_end:
                    diff = self._update(root.right_top, row, col, val)
        elif row_mid + 1 <= root.row_end:
            if col_mid >= col:
                diff = self._update(root.left_bottom, row, col, val)
            else:
                if col_mid + 1 <= root.col_end:
                    diff = self._update(root.right_bottom, row, col, val)

        root.sum += diff

        return diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._sumRegion(self.root, row1, col1, row2, col2)

    def _sumRegion(self, root, row1, col1, row2, col2):
        if root.row_start == row1 and root.row_end == row2 and root.col_start == col1 and root.col_end == col2:
            return root.sum

        row_mid = (root.row_start + root.row_end) // 2
        col_mid = (root.col_start + root.col_end) // 2

        _sum = 0
        if row_mid >= row2:
            if col_mid >= col2:
                _sum = self._sumRegion(root.left_top, row1, col1, row2, col2)
            elif col_mid < col1:
                if root.right_top:
                    _sum = self._sumRegion(
                        root.right_top, row1, col1, row2, col2)
            else:
                _sum = self._sumRegion(
                    root.left_top, row1, col1, row2, col_mid)
                if root.right_top:
                    _sum += self._sumRegion(root.right_top,
                                            row1, col_mid + 1, row2, col2)
        elif row_mid < row1:
            if root.left_bottom:
                if col_mid >= col2:
                    _sum = self._sumRegion(
                        root.left_bottom, row1, col1, row2, col2)
                elif col_mid < col1:
                    if root.right_bottom:
                        _sum = self._sumRegion(
                            root.right_bottom, row1, col1, row2, col2)
                else:
                    _sum = self._sumRegion(
                        root.left_bottom, row1, col1, row2, col_mid)
                    if root.right_bottom:
                        _sum += self._sumRegion(root.right_bottom,
                                                row1, col_mid + 1, row2, col2)
        else:
            if col_mid >= col2:
                _sum = self._sumRegion(
                    root.left_top, row1, col1, row_mid, col2)
                if root.left_bottom:
                    _sum += self._sumRegion(root.left_bottom,
                                            row_mid + 1, col1, row2, col2)
            elif col_mid < col1:
                if root.right_top:
                    _sum = self._sumRegion(
                        root.right_top, row1, col1, row_mid, col2)
                    if root.right_bottom:
                        _sum += self._sumRegion(root.right_bottom,
                                                row_mid + 1, col1, row2, col2)
            else:
                _sum = self._sumRegion(
                    root.left_top, row1, col1, row_mid, col_mid)
                if root.right_top:
                    _sum += self._sumRegion(root.right_top,
                                            row1, col_mid + 1, row_mid, col2)
                if root.left_bottom:
                    _sum += self._sumRegion(root.left_bottom,
                                            row_mid + 1, col1, row2, col_mid)
                if root.right_bottom:
                    _sum += self._sumRegion(root.right_bottom,
                                            row_mid + 1, col_mid + 1, row2, col2)

        return _sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
