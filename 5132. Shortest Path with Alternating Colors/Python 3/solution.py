class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for edge in red_edges:
            src, dest = edge[0], edge[1]
            red[src].append(dest)
        for edge in blue_edges:
            src, dest = edge[0], edge[1]
            blue[src].append(dest)

        queue = collections.deque()
        result = [float('inf')] * n

        queue.append((0, 0, 'b'))
        visited = set()
        visited.add((0, 'b'))
        visited.add((0, 'r'))
        queue.append((0, 0, 'r'))
        while queue:
            node, length, color = queue.popleft()
            result[node] = min(result[node], length)
            if color == 'b':
                nxt_list = red[node]
                nxt_color = 'r'
            else:
                nxt_list = blue[node]
                nxt_color = 'b'
            for nxt in nxt_list:
                if (nxt, nxt_color) not in visited:
                    queue.append((nxt, length + 1, nxt_color))
                    visited.add((nxt, nxt_color))

        for idx, ele in enumerate(result):
            if ele == float('inf'):
                result[idx] = -1

        return result
