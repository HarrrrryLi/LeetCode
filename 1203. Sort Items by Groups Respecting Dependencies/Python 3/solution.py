class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graphs = {}
        group_graph = collections.defaultdict(set)
        gcnt = 0
        for idx, g in enumerate(group):
            if g == -1:
                g = m + gcnt
                group[idx] = g
                gcnt += 1
            if g not in graphs:
                graphs[g] = collections.defaultdict(set)

        for idx in range(n):
            cur_group = group[idx]
            if idx not in graphs[cur_group]:
                graphs[cur_group][idx] = set()
            if cur_group not in group_graph:
                group_graph[cur_group] = set()
            for before in beforeItems[idx]:
                if cur_group == group[before]:
                    graphs[cur_group][before].add(idx)
                else:
                    group_graph[group[before]].add(cur_group)

        if not self.isAcyclic(group_graph):
            return []

        group_order = []
        visited = set()
        for group in group_graph:
            if group in visited:
                continue
            self.toposort(group, group_graph, group_order, visited)
        group_order.reverse()

        result = []
        for group in group_order:
            if not self.isAcyclic(graphs[group]):
                return []
            inner = []
            visited = set()
            for item in graphs[group]:
                if item in visited:
                    continue
                self.toposort(item, graphs[group], inner, visited)

            result.extend(reversed(inner))

        return result

    def isAcyclic(self, graph):
        for key in graph:
            stack = collections.deque()
            stack.append((key, set()))
            while stack:
                cur, path = stack.pop()
                for nxt in graph[cur]:
                    if nxt in path:
                        return False
                    temp = set(path)
                    temp.add(cur)
                    stack.append((nxt, temp))
        return True

    def toposort(self, cur, graph, result, visited):
        visited.add(cur)

        for nxt in graph[cur]:
            if nxt in visited:
                continue
            self.toposort(nxt, graph, result, visited)

        result.append(cur)
