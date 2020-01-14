Convert the number to string s. Find the highest digit of 0 called the index of that is idx. The minimum number should be int(s[idx + 1 : 0]) + 1. Otherwise it should be 1. One more thing is if the number ends with 1, it should be at least 2. Then go through from start number to half of n.


Time Complexity O(NlogN). Space Complexity O(logN)