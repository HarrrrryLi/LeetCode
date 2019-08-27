class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        size = len(graph)
        result = []
        stack = collections.deque()
        stack.append((0, [0]))

        while stack:
            cur, path = stack.pop()
            if cur == size - 1:
                result.append(path)

            for nxt in graph[cur]:
                temp = list(path)
                temp.append(nxt)
                stack.append((nxt, temp))

        return result
