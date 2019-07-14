DP.

Go through the list. record score, when it's greater than 8 plus 1, else minus 1.


If score is greater than 0 means this well-performance interval from beginning, then result = index.

Put the first time appear index of score into a dictionary. If score - 1 in dictionary means from that index to current index, tiring day is more than non-tiring day. So this intervel is well performance interval

Time Complexity O(n), Space Complexity O(n)