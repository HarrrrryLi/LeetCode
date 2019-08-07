class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for s, d, c in flights:
            graph[s].append((d, c))

        heap = []
        heapq.heappush(heap, (0, 0, src))

        while heap:
            cost, stops, cur = heapq.heappop(heap)
            if cur == dst:
                return cost
            if stops - 1 >= K:
                continue
            for d, c in graph[cur]:
                heapq.heappush(heap, (cost + c, stops + 1, d))

        return -1
