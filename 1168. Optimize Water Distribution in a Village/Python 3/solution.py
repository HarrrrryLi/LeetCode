class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        pipecost = collections.defaultdict(list)

        for h1, h2, cost in pipes:
            pipecost[h1].append((cost, h2))
            pipecost[h2].append((cost, h1))

        heap = []
        visited = set()
        for idx, well in enumerate(wells):
            heapq.heappush(heap, (well, idx + 1))

        result, starthouse = heapq.heappop(heap)
        visited.add(starthouse)
        for c, h in pipecost[starthouse]:
            heapq.heappush(heap, (c, h))

        while heap and len(visited) < n:
            cost, current = heapq.heappop(heap)
            if current in visited:
                continue
            visited.add(current)
            result += cost
            if len(visited) == n:
                break
            for c, h in pipecost[current]:
                heapq.heappush(heap, (c, h))

        return result
