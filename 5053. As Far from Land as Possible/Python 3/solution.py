class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        size = len(grid)
        record = {}
        queue = collections.deque()

        for row in range(size):
            for col in range(size):
                if grid[row][col]:
                    queue.append((row, col, 0))

        if not queue:
            return -1

        pattern = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            row, col, dist = queue.popleft()
            for deltar, deltac in pattern:
                nxtr, nxtc = row + deltar, col + deltac
                if nxtr >= 0 and nxtr < size and nxtc >= 0 and nxtc < size:
                    if not grid[nxtr][nxtc]:
                        if (nxtr, nxtc) not in record or dist + 1 < record[(nxtr, nxtc)]:
                            queue.append((nxtr, nxtc, dist + 1))
                            record[(nxtr, nxtc)] = dist + 1

        if not record:
            return -1

        return max(record.values())
