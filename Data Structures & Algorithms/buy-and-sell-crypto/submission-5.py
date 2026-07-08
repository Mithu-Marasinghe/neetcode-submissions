class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_val = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                gain = prices[r] - prices[l]
                max_val = max(max_val, gain)
                r += 1
        return max_val