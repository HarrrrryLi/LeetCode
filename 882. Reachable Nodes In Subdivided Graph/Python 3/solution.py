class Solution(object):
    def reachableNodes(self, edges, M, N):
        graph = collections.defaultdict(dict)
        for node1, node2, nums in edges:
            graph[node1][node2] = nums
            graph[node2][node1] = nums

        heap = [(0, 0)]
        dist = {0: 0}
        used = {}
        result = 0

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            result += 1

            for dest, weight in graph[node].items():
                v = min(weight, M - d)
                used[node, dest] = v

                nxtd = d + weight + 1
                if nxtd < dist.get(dest, M + 1):
                    heapq.heappush(heap, (nxtd, dest))
                    dist[dest] = nxtd

        for node1, node2, nums in edges:
            result += min(nums, used.get((node1, node2), 0) +
                          used.get((node2, node1), 0))

        return result
