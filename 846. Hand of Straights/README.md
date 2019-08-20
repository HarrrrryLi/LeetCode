DP.

For each letter store its frequency. Sort all unique letters.

For each number n, if its frequency isn't 0, check whether frequency of every number is not smaller than freq[n], if it's not return False, if it is, update this frequency by minus freq[n].


Time Complexity O(max(NlogN, N * W)) Space Complexity O(N)