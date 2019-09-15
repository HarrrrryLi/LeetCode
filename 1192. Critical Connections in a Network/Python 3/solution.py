class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for p1, p2 in connections:
            graph[p1].append(p2)
            graph[p2].append(p1)

        visited = [False] * (n)
        discover_time = [float("Inf")] * (n)
        min_time = [float("Inf")] * (n)
        parent = [-1] * (n)

        result = []
        time = [0]
        for i in range(n):
            if visited[i] == False:
                result.extend(self.bridgeUtil(i, visited, parent,
                                              min_time, discover_time, time, graph))
        return result

    def bridgeUtil(self, cur, visited, parent, min_time, discover_time, time, graph):
        visited[cur] = True
        discover_time[cur] = time[0]
        min_time[cur] = time[0]
        time[0] += 1
        result = []
        for nxt in graph[cur]:
            if visited[nxt] == False:
                parent[nxt] = cur
                find = self.bridgeUtil(
                    nxt, visited, parent, min_time, discover_time, time, graph)
                result.extend(find)
                min_time[cur] = min(min_time[cur], min_time[nxt])
                if min_time[nxt] > discover_time[cur]:
                    result.append([cur, nxt])
            elif nxt != parent[cur]:
                min_time[cur] = min(min_time[cur], discover_time[nxt])
        return result
