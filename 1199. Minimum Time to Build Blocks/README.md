Using heap.

For each case, we can choose [1, remain_works - workers] worker to split.  If all the remain task have the same value then (remain_works - workers) workers need to split.


Time Complexity O((N ^ N) * NlogN). Space Complexity O((N ^ N) * NlogN)