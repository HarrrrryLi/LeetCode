DP

For each idx in dp array, the number means how many substring end with this index/letter. Then update those value on the right, if the letter is first seen(make sure there is no duplicate). The sum of dp array is the total number of distince substring.

Time Complexity O(N ^ 2). Space Complexity O(N)