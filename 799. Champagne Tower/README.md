BFS

For arbitrary row, n the cup will influence n th and n + 1 th cups in next row. So we can find query cup will be influence by glass - (query_row - r). We can only expand those cups.


Time Complexity O(N). Space Complexity O(N)