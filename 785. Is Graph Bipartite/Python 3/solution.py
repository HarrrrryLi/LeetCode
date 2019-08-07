class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        groups = [set(), set()]
        size = len(graph)
        groupid = {0: 0}
        visited = set()
        for idx in range(size):
            if idx in visited:
                continue
            stack = collections.deque()
            stack.append(idx)
            while stack:
                cur = stack.pop()
                if cur in groupid:
                    gid = groupid[cur]
                else:
                    gid = 0
                nodes = graph[cur]
                for node in nodes:
                    if node in groups[gid]:
                        return False
                    else:
                        if node not in visited:
                            groups[1 - gid].add(node)
                            groupid[node] = 1 - gid
                            visited.add(node)
                            stack.append(node)

        return True
