class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        # 스택이용
        max_price = prices.pop()
        while prices:
            price = prices.pop()
            if max_price <= price:
                max_price = price
            else:
                ans = max(ans, max_price - price)
        return ans        