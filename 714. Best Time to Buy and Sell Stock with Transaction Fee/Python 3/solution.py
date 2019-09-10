class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        low = prices[0]
        ans = 0
        for price in prices:
            if price < low:
                low = price
            elif price - fee - low > 0:
                ans += price - fee - low
                low = price - fee
        return ans
