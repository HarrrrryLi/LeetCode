DP.

For index i, which can influence that num is i - K to i - 1.  After flips, if it's 0, flip number add 1. update dp[i] = cur.

If number is 0 and i > size - K, then return -1


Time Complexity O(N). Space Complexity O(N)