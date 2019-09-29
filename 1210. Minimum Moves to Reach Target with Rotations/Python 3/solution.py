class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        size = len(grid)
        result = float('inf')
        visited = {}
        visited[((0, 0), (0, 1))] = 0
        heap = []
        heapq.heappush(heap, (2 * size - 3 + 2 * size - 3, 0, (0, 0), (0, 1)))

        while heap:
            dist, steps, (tr, tc), (hr, hc) = heapq.heappop(heap)
            if dist == 0:
                result = min(steps, result)
            if steps >= result:
                continue

            if tr + 1 < size and grid[tr + 1][tc] == 0 and hr + 1 < size and grid[hr + 1][hc] == 0:
                if ((tr + 1, tc), (hr + 1, hc)) not in visited or visited[((tr + 1, tc), (hr + 1, hc))] > steps + 1:
                    d = self.calculatedist(tr + 1, tc, hr + 1, hc, size)
                    heapq.heappush(
                        heap, (d, steps + 1, (tr + 1, tc), (hr + 1, hc)))
                    visited[((tr + 1, tc), (hr + 1, hc))] = steps + 1
                if self.ishorizontal(tr, hr):
                    if ((tr, tc), (tr + 1, tc)) not in visited or visited[((tr, tc), (tr + 1, tc))] > steps + 1:
                        d = self.calculatedist(tr, tc, tr + 1, tc, size)
                        heapq.heappush(
                            heap, (d, steps + 1, (tr, tc), (tr + 1, tc)))
                        visited[((tr, tc), (tr + 1, tc))] = steps + 1

            if tc + 1 < size and grid[tr][tc + 1] == 0 and hc + 1 < size and grid[hr][hc + 1] == 0:
                if ((tr, tc + 1), (hr, hc + 1)) not in visited or visited[((tr, tc + 1), (hr, hc + 1))] > steps + 1:
                    d = self.calculatedist(tr, tc + 1, hr, hc + 1, size)
                    heapq.heappush(
                        heap, (d, steps + 1, (tr, tc + 1), (hr, hc + 1)))
                    visited[((tr, tc + 1), (hr, hc + 1))] = steps + 1

                if not self.ishorizontal(tr, hr):
                    if ((tr, tc), (tr, tc + 1)) not in visited or visited[((tr, tc), (tr, tc + 1))] > steps + 1:
                        d = self.calculatedist(tr, tc, tr, tc + 1, size)
                        heapq.heappush(
                            heap, (d, steps + 1, (tr, tc), (tr, tc + 1)))
                        visited[((tr, tc), (tr, tc + 1))] = steps + 1

        if result == float('inf'):
            return -1

        return result

    def calculatedist(self, tr, tc, hr, hc, size):
        return size - 1 - tr + abs(size - 2 - tc) + size - 1 - hr + size - 1 - hc

    def ishorizontal(self, tr, hr):
        if tr == hr:
            return True
        return False
