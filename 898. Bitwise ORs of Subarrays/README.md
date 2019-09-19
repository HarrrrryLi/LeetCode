Using DP.  Each element is a set. Starting with 0.

for each number, current set is equal to every number in previous bit-or with current number. Also we need to include current number.

Time Complexity O(N * log W). Space Complexity O(log W). W is how many bits it has.