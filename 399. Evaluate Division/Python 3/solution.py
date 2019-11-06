class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        size = len(equations)
        graph = collections.defaultdict(list)

        for idx in range(size):
            num, deno = equations[idx]
            div = values[idx]
            graph[num].append((deno, div))
            graph[deno].append((num, 1 / div))

        result = []
        for num, deno in queries:
            if num not in graph:
                result.append(-1.0)
                continue
            if deno not in graph:
                result.append(-1.0)
                continue
            visited = set()
            stack = collections.deque()
            stack.append((num, 1.0))
            visited.add(num)

            while stack:
                cur, div = stack.pop()
                if cur == deno:
                    result.append(div)
                    break
                for nxt, v in graph[cur]:
                    if nxt not in visited:
                        stack.append((nxt, v * div))
                        visited.add(nxt)
            else:
                result.append(-1.0)

        return result
