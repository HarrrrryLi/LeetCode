class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = collections.defaultdict(list)
        for idx1, idx2 in pairs:
            i1 = bisect.bisect(graph[idx1], idx2)
            graph[idx1].insert(i1, idx2)

            i2 = bisect.bisect(graph[idx2], idx1)
            graph[idx2].insert(i2, idx1)

        groups = []
        visited = set()
        size = len(s)
        for idx in range(size):
            if idx not in visited:
                stack = collections.deque()
                stack.append(idx)
                visited.add(idx)
                group = set()
                group.add(idx)
                while stack:
                    cur = stack.pop()
                    for nxt in graph[cur]:
                        if nxt not in visited:
                            stack.append(nxt)
                            visited.add(nxt)
                            group.add(nxt)
                groups.append(group)

        result = ['a'] * size
        for group in groups:
            letters = [s[idx] for idx in group]
            letters.sort()
            for i, idx in enumerate(sorted(group)):
                result[idx] = letters[i]

        return ''.join(result)
