class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        row_size, col_size = len(matrix), len(matrix[0])
        graph = collections.defaultdict(set)
        degrees = collections.Counter()
        pattern = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row in range(row_size):
            for col in range(col_size):
                if (row, col) not in graph:
                    graph[(row, col)] = set()
                if (row, col) not in degrees:
                    degrees[(row, col)] = 0

                for dr, dc in pattern:
                    nxtr, nxtc = row + dr, col + dc
                    if self.checkValid(nxtr, nxtc, row_size, col_size):
                        if matrix[nxtr][nxtc] > matrix[row][col]:
                            graph[(row, col)].add((nxtr, nxtc))
                            degrees[(nxtr, nxtc)] += 1

        queue = collections.deque()
        for row in range(row_size):
            for col in range(col_size):
                if degrees[(row, col)] == 0:
                    queue.append(((row, col), 1))

        result = 0
        while queue:
            cur, depth = queue.popleft()
            result = max(result, depth)
            for nxt in graph[cur]:
                degrees[nxt] -= 1
                if degrees[nxt] == 0:
                    queue.append((nxt, depth + 1))

        return result

    def checkValid(self, row, col, row_size, col_size):
        if 0 <= row < row_size and 0 <= col < col_size:
            return True

        return False
