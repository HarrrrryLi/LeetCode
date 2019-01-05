First, sort the string list with key = lambda x: (counter(x), x). Where counter the map count the frequency of each letter
Then, result[::2], result[1::2] = sortedlist[N/2:], sortedlist[N/2:]

Time Complexity O(NlogN). Space complexity O(N)