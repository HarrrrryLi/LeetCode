Using Binary Search.

First sort this array (don't do inplace sorting). For each num in origin array, find index in the new array, pop it out.
Then find insect index of (num + 1) // 2, result add this index

Time Complexity O(NlogN). Space Complexity O(N)