class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build graph
        size = len(words)
        graph = collections.defaultdict(set)
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        for cnt in range(1, size):
            word1 = words[cnt - 1]
            word2 = words[cnt]
            word_size = min(len(word1), len(word2))
            for idx in range(word_size):
                c1, c2 = word1[idx], word2[idx]
                if c1 == c2:
                    continue
                else:
                    graph[c1].add(c2)
                    break

        # check acycle
        for c in graph:
            stack = collections.deque()
            parents = set()
            stack.append((c, parents))
            while stack:
                cur, p = stack.pop()
                for nxt in graph[cur]:
                    if nxt in p:
                        print(nxt)
                        return ''
                    else:
                        temp = set(p)
                        temp.add(cur)
                        stack.append((nxt, temp))

        # topological sort
        visited = set()
        result = []
        for c in graph:
            if c not in visited:
                self.toposort(c, visited, graph, result)

        result.reverse()
        return ''.join(result)

    def toposort(self, parent, visited, graph, result):
        visited.add(parent)

        for child in graph[parent]:
            if child not in visited:
                self.toposort(child, visited, graph, result)

        result.append(parent)
