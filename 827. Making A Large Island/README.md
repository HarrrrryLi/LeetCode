First simply search all islands record their area and the island label(I use start grid as label)

If there is no island, initial result with 0, or initial result with max area of islands

Secondly go through all water cell, suppose it becomes island, then it will connect all islands in four direction. Add all unique islands area to 1. update result.

Time Complexity O(W * H). Space Complexity O(W * H)