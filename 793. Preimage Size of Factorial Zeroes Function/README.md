If given x to calculate f(x), we only need to count the number of 5. (Acutally it's min(number of 5, number of 2), but always 5 appears less). We can find that f(5 ^ (N + 1)) = 5 * f(5 ^ N) + 1. Because when it has the fifth 5 ^ N, it will have one more 5.

Then we can see if given K, there are only two outputs. If K exists, it's 5. If K doesn't exists, it's 0.

So first, go through power of 5, find N which f(5 ^ N) <= K and f(5 ^ (N + 1)) > K
If f(5 ^ N) == K, means it exists, return 5.

Otherwise, check K % f(5 ^ N). If the mod is 0 and K / f(5 ^ N) != 5, means it exists return 5. If the mode is 0 and K / f(5 ^ N) == 5, means it doesn't exists, return 0. If the mod is not 0 K % = f(5 ^ N) and update N until f(5 ^ N) <= K.


Time Complexity O(logK). Space Complexity O(1)