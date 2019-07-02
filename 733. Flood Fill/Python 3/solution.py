import collections


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:

        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        row_size = len(image)
        col_size = len(image[0])
        pattern = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        stack = collections.deque()
        stack.append((sr, sc))

        while stack:
            row, col = stack.pop()
            image[row][col] = newColor

            for incr, incc in pattern:
                nxt_row, nxt_col = row + incr, col + incc
                if nxt_row >= 0 and nxt_row < row_size\
                        and nxt_col >= 0 and nxt_col < col_size\
                        and image[nxt_row][nxt_col] == oldColor:
                    stack.append((nxt_row, nxt_col))

        return image
