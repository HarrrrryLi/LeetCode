class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        d = query_row - query_glass
        queue = collections.deque()
        queue.append([0, 0, poured])
        while queue:
            r, c, w = queue.popleft()
            if r == query_row and c == query_glass:
                return min(1.0, w)
            if w > 1.0 and c >= (r - d) and c <= query_glass:
                w = (w - 1.0) / 2.0
                if queue and queue[-1][1] == c:
                    queue[-1][2] += w
                else:
                    queue.append([r + 1, c, w])
                queue.append([r + 1, c + 1, w])
        return 0.0
