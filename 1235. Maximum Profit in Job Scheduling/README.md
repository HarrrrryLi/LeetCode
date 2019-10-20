First sort the lists together.

Create a dp list. each element means, the maximum profit it can make exactly a job end at this time.
We maintain a variable called current_max means, until now, the maximum profit(don't need to end at this time exactly). We also need to record previous time when the current_max update, called this variable pre.

Then go through lists. we can get current_max at start time. Next we can update dp[end] as max(dp[end], current_max + profit). Then we update pre as start.

At the end, we need to go through from pre to the end of dp list.

Time Complexity O(max(NlogN, L)) Space Complexity O(L). N is the length of the lists. L is the latest end time.