Using heap.

Suppose we don't add any fuel at all stations. Just add fuel into max heap.

When we reach a station, if we find that the fuel is negative, that means to reach this position we need to add some fuel before. Then get the largest fuel(greedy). If we add all fuel in all previous stations and the fuel is still negative, means we can't reach this station and target.

Time Complexity O(NlogN). Space Complexity O(N)