Math Problem. Define x is the start number, n is the length.

We can get

(x + x + n - 1) * n / 2 = N

After transform we can get
x = (2 * N - n * (n - 1)) / (2 * n)

Go through all possible n, calculate x, if x is positive integer, result += 1

Time Complexity O(N) Space Complexity O(1)