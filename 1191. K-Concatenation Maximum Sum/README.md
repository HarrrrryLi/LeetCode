First calculate maximum sum subarray(using dp, dp array called dp) and sum array(using dp, dp array called _sum) for original array. 

Then the result situation will in following situations:
    1. 0
    2. maximum sum subarray for original array
    3. dp[-1] + (k - 2) * sum + max(_sum)


Time Complexity O(N). Space Complexity O(N)