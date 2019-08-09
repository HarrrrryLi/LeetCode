class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])

        queue = collections.deque()

        total_fresh = 0

        for row_cnt in range(row_size):
            for col_cnt in range(col_size):
                if grid[row_cnt][col_cnt] == 1:
                    total_fresh += 1
                elif grid[row_cnt][col_cnt] == 2:
                    queue.append((row_cnt, col_cnt, 0))

        result = 0

        while queue and total_fresh:
            while queue and queue[0][2] == result and total_fresh:
                row, col, time = queue.popleft()
                if row + 1 < row_size and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    total_fresh -= 1
                    queue.append((row + 1, col, time + 1))
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    total_fresh -= 1
                    queue.append((row - 1, col, time + 1))
                if col + 1 < col_size and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    total_fresh -= 1
                    queue.append((row, col + 1, time + 1))
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    total_fresh -= 1
                    queue.append((row, col - 1, time + 1))
            result += 1

        if total_fresh:
            return -1

        return result
