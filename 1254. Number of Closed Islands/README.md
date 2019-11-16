DFS. An island is not closed when there is a cell reach the boundary of the matrix(eg: row is 0 or row_size or col is 0 or col_size).


PS: When found a cell reach the boundary, don't break, finished the search but don't add it to result.


Time Complexity O(W * H). Space Complexity O(W * H)