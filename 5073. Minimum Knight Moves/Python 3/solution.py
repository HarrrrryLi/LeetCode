class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        patterns = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                    (-1, -2), (-2, -1), (1, -2), (2, -1)]
        visited = set()
        queue = collections.deque()
        queue.append((0, 0, 0))
        visited.add((0, 0))

        while queue:
            row, col, steps = queue.popleft()
            dist = abs(row - x) + abs(col - y)
            if row == x and col == y:
                return steps

            for dr, dc in patterns:
                nxtr, nxtc = row + dr, col + dc
                nxt_dist = abs(nxtr - x) + abs(nxtc - y)
                if nxt_dist <= dist and (nxtr, nxtc) not in visited:
                    visited.add((nxtr, nxtc))
                    queue.append((nxtr, nxtc, steps + 1))

        return -1
