Sliding window.

First convert position list to time list. Then using sliding window, window size is K + 1. If all the time in the sliding window is smaller than the left and right boundary, this situation is what we need.


Time Complexity O(N). Space Complexity O(N)