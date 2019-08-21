class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])

        stack = collections.deque()
        visited = set()
        pattern = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        union = {}
        record = {}
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] and (row, col) not in visited:
                    stack.append((row, col))
                    visited.add((row, col))
                    union[(row, col)] = (row, col)
                    temp = 1
                    while stack:
                        curr, curc = stack.pop()
                        for dr, dc in pattern:
                            nxtr, nxtc = curr + dr, curc + dc
                            if nxtr >= 0 and nxtr < row_size and nxtc >= 0 and nxtc < col_size:
                                if grid[nxtr][nxtc] and (nxtr, nxtc) not in visited:
                                    stack.append((nxtr, nxtc))
                                    visited.add((nxtr, nxtc))
                                    union[(nxtr, nxtc)] = (row, col)
                                    temp += 1
                    record[(row, col)] = temp

        if not record:
            result = 0
        else:
            result = max(record.values())

        for row in range(row_size):
            for col in range(col_size):
                if not grid[row][col]:
                    temp = 1
                    connected = set()
                    for dr, dc in pattern:
                        nxtr, nxtc = row + dr, col + dc
                        if nxtr >= 0 and nxtr < row_size and nxtc >= 0 and nxtc < col_size and grid[nxtr][nxtc]:
                            island = union[(nxtr, nxtc)]
                            if island not in connected:
                                temp += record[island]
                                connected.add(island)
                    result = max(temp, result)

        return result
