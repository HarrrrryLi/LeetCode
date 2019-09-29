class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        size = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        degree = {}
        for mouse in range(size):
            for cat in range(size):
                degree[mouse, cat, MOUSE] = len(graph[mouse])
                degree[mouse, cat, CAT] = len(graph[cat]) - (0 in graph[cat])

        queue = collections.deque()  # mouse location, cat location, move, result
        for cat in range(size):
            for move in (CAT, MOUSE):
                color[0, cat, move] = MOUSE
                queue.append((0, cat, move, MOUSE))
                if cat > 0:
                    color[cat, cat, move] = CAT
                    queue.append((cat, cat, move, CAT))

        while queue:
            mouse, cat, move, result = queue.popleft()
            for nxtmouse, nxtcat, nxtmove in self.children(mouse, cat, move, graph):
                if color[nxtmouse, nxtcat, nxtmove] == DRAW:
                    if nxtmove == result:
                        color[nxtmouse, nxtcat, nxtmove] = result
                        queue.append((nxtmouse, nxtcat, nxtmove, result))
                    else:
                        degree[nxtmouse, nxtcat, nxtmove] -= 1
                        if degree[nxtmouse, nxtcat, nxtmove] == 0:
                            color[nxtmouse, nxtcat, nxtmove] = 3 - nxtmove
                            queue.append(
                                (nxtmouse, nxtcat, nxtmove, 3 - nxtmove))

        return color[1, 2, 1]

    def children(self, mouse, cat, move, graph):
        if move == 2:
            for mnxt in graph[mouse]:
                yield mnxt, cat, 3 - move
        else:
            for cnxt in graph[cat]:
                if cnxt:
                    yield mouse, cnxt, 3 - move
