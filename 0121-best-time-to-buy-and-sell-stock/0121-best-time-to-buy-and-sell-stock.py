class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices:  
            profit = price - min_price
            max_profit = max(profit, max_profit)
            min_price = min(min_price, price)

        return max_profit
