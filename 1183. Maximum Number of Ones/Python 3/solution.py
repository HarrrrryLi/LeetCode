class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        if width < height:
            width, height = height, width

        x, x0 = divmod(width, sideLength)
        v, v0 = divmod(height, sideLength)
        kount = [x0 * v0, (sideLength - x0) * v0, x0 *
                 (sideLength - v0), (sideLength - x0) * (sideLength - v0)]

        value = [(x + 1) * (v + 1), x * (v + 1), (x + 1) * v, x * v]

        print(kount)
        print(value)
        # Sum the largest ones
        ans = 0
        for k, n in zip(kount, value):
            print(maxOnes, k, n)
            if maxOnes > k:
                ans += k * n
                maxOnes -= k
            else:
                return ans + maxOnes * n
        return ans
