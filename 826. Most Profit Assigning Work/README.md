DP.

First sort difficulty with index (don't use index as key). 

Then go through sorted difficulty list, get max profit of all tasks whose difficulties are not greater than current one.


For each worker, using bisect find the position/ max profit that worker can get.


Time Complexity O(NlogN). Space Complexity O(N)