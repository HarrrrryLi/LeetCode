2D DP.

The result will be sum(s) + sum(t) - max_common_letters_sum. What we need to calculate is max_common_letters_sum. 

If s1[cnt1 - 1] == s2[cnt2 - 1], dp[cnt1][cnt2] = dp[cnt1 - 1][cnt2 - 1] - 2 * ord(s1[cnt1 - 1])
Otherwise, it should be the max value of dp[cnt1 - 1][cnt2] and dp[cnt1][cnt2 - 1]

Time Complexity O(L1 * L2). Space Complexity O(L1 * L2) 