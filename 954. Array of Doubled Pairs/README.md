First using counter to count freq of each num.

If the number of 0 is odd, return False.
Otherwise, check the minimum number whether 2 * minimum number is in the counter. If not, return False. Otherwise for frequency of both minimum number and its twice minus one. If freq of any number equals 0, delete that number.


Time Complexity O(N ^ 2). Space Complexity O(N)