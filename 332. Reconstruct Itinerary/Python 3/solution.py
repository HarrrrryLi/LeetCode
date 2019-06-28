import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = collections.defaultdict(list)
        tickets.sort()
        for dep, arr in tickets:
            graph[dep].append(arr)
        result = []
        self.dfs(graph, 'JFK', result)
        return result

    def dfs(self, graph, dep, path):
        while graph[dep]:
            self.dfs(graph, graph[dep].pop(0), path)
        path.insert(0, dep)
