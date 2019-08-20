class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        g = {idx: neighbors for idx, neighbors in enumerate(graph)}
        size = len(graph)
        if size == 1:
            return 0
        heap = []
        lowest_freq = min([len(l) for l in g.values()])
        if lowest_freq == size - 1:
            return size - 1

        for node in range(size):
            if len(g[node]) == lowest_freq:
                heapq.heappush(heap, (0, 0, node, {node}, set()))

        result = float('inf')
        while heap:
            visited_nodes, length, cur, path, visited_edges = heapq.heappop(
                heap)
            if -visited_nodes == size:
                result = min(result, length)
                continue
            if length >= result:
                continue
            for neighbor in g[cur]:
                if (cur, neighbor) not in visited_edges:
                    temp = set(path)
                    temp.add(neighbor)
                    ve = set(visited_edges)
                    ve.add((cur, neighbor))
                    heapq.heappush(
                        heap, (-len(temp), length + 1, neighbor, temp, ve))

        if result == float('inf'):
            return 0
        return result
