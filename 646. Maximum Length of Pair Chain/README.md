Sort list according to the end time. create a new list only contains sorted end time.

Using bisect_left to find the insection point of start time in the end time list. dp[idx] = max(dp[:i]) + 1

return max(dp)

Time Complexity O(N ^ 2). Space Complexity O(N)