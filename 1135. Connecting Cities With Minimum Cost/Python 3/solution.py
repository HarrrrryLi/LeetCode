class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        visited = set()
        result = 0
        for city1, city2, cost in connections:
            graph[city1].append((cost, city2))
            graph[city2].append((cost, city1))

        start = connections[0][0]
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            cost, city = heapq.heappop(heap)
            if city not in visited:
                visited.add(city)
                result += cost
                for nxt_cost, nxt_city in graph[city]:
                    heapq.heappush(heap, (nxt_cost, nxt_city))

        if len(visited) != N:
            return -1

        return result
