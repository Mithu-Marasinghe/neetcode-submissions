class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_value = 0

        while r < len(prices):
            print(prices[l], prices[r])
            if (prices[r] < prices[l]):
                l = r
                r += 1
            else:
                gain = prices[r] - prices[l]
                max_value = max(gain, max_value)
                r += 1
        return max_value