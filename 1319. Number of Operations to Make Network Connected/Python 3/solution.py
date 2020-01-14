class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        visited = set()
        candidates = set(range(n))
        graph = collections.defaultdict(set)

        for com1, com2 in connections:
            graph[com1].add(com2)
            graph[com2].add(com1)

        result = -1
        stack = collections.deque()

        for num in range(n):
            if num in visited:
                continue
            stack.append(num)
            visited.add(num)
            result += 1
            while stack:
                cur = stack.pop()
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)

        return result
