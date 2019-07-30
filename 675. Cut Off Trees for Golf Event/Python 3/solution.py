class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        row_size, col_size = len(forest), len(forest[0])
        heap = []
        for row in range(row_size):
            for col in range(col_size):
                height = forest[row][col]
                if height > 1:
                    heapq.heappush(heap, (height, row, col))
        pre_row, pre_col = 0, 0
        result = 0
        record = {}
        while heap:
            _, row, col = heapq.heappop(heap)
            steps = self.search_path(
                forest, (pre_row, pre_col), (row, col), record)
            if steps == -1:
                return -1
            result += steps
            pre_row, pre_col = row, col

        return result

    def search_path(self, forest, start, end, record):
        if (start, end) in record:
            return record[(start, end)]
        row_size, col_size = len(forest), len(forest[0])
        queue = collections.deque()
        visited = set()
        visited.add(start)
        queue.append((start, 0))

        while queue:
            current, steps = queue.popleft()
            if current == end:
                return steps
            row, col = current
            if row - 1 >= 0 and (row - 1, col) not in visited and forest[row - 1][col] > 0:
                queue.append(((row - 1, col), steps + 1))
                visited.add((row - 1, col))
            if row + 1 < row_size and (row + 1, col) not in visited and forest[row + 1][col] > 0:
                queue.append(((row + 1, col), steps + 1))
                visited.add((row + 1, col))
            if col - 1 >= 0 and (row, col - 1) not in visited and forest[row][col - 1] > 0:
                queue.append(((row, col - 1), steps + 1))
                visited.add((row, col - 1))
            if col + 1 < col_size and (row, col + 1) not in visited and forest[row][col + 1] > 0:
                queue.append(((row, col + 1), steps + 1))
                visited.add((row, col + 1))
        return -1
