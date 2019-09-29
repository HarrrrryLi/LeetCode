Math Problem. Target Function can be written as 
arr1[i] + arr1[i] + i - (arr1[j] + arr1[j] + j) OR
arr1[i] - arr1[i] + i - (arr1[j] - arr1[j] + j) OR
-arr1[i] + arr1[i] + i - (-arr1[j] + arr1[j] + j) OR
-arr1[i] - arr1[i] + i - (-arr1[j] - arr1[j] + j) OR
And abs function should be the largest one in these four values.


Seperatly store four formula result for each num into a list.
Then calculate max - min of each list. Next, get max value of four values.

Time Complexity O(n). Space Complexity O(n)