class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])
        visited = set()
        pattern = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = 0

        for row in range(row_size):
            for col in range(col_size):
                if not grid[row][col] and (row, col) not in visited:
                    isClosed = True
                    stack = collections.deque()
                    stack.append((row, col))
                    visited.add((row, col))

                    while stack:
                        r, c = stack.pop()
                        if r == 0 or c == 0 or r == row_size - 1 or c == col_size - 1:
                            isClosed = False
                        for dr, dc in pattern:
                            nxtr, nxtc = r + dr, c + dc
                            if 0 <= nxtr < row_size and 0 <= nxtc < col_size and not grid[nxtr][nxtc] and (nxtr, nxtc) not in visited:
                                stack.append((nxtr, nxtc))
                                visited.add((nxtr, nxtc))
                    if isClosed:
                        result += 1

        return result
