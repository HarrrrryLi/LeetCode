Using dp. 

Sort list first. Create a set which contains all elements in the list.

Then go through list, for each number, we regard it as root.  Next, search in the set, if left and right are both in the set, the total number of trees equals 1 + dp[left_num] * dp[right_num]


return sum of dp modulo (10 ** 9 + 7)

Time Complexity O(N^2) Time Complexity O(N)