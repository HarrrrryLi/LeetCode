2D DP
Build a 2D array. dp[row_cnt][col_cnt] = nums means word1[:row_cnt + 1] needs nums step to get word2[:col_cnt + 1]. So dp[row_cnt][0] = row_cnt, dp[0][col_cnt] = col_cnt

If word1[row_cnt] = word2[col_cnt], dp[row_cnt][col_cnt] = dp[row_cnt - 1][col_cnt - 1]  (Do not need any change for this position)

Else, dp[row_cnt][col_cnt] = min(dp[row_cnt - 1][col_cnt - 1], dp[row_cnt - 1][col_cnt], dp[row_cnt][col_cnt - 1]) + 1
(Represent replace, delete, add operations)

Time Complexity O(n^2) Space Complexity O(n^2)