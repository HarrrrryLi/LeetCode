DP.


dp[m][k] represents m moves and k egges can check dp[m][k] floors
 
assume dp[m - 1][k - 1] = n0, dp[m - 1][k] = n1
we drop an egg at dp[m - 1][k - 1] + 1 floor
if it breaks, we can check the lower floors in [1, n0]
if it survives, we can check the higher floors in [n0 + 1, n1 + n0 + 1]

so we can check floors in [1, n1 + n0 + 1] which is dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1


Time Complexity O(N * K). Space Complexity O(N * K)