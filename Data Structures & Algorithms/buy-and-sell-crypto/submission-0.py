import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        while l < len(prices):
            best = 0
            r = len(prices)-1
            while r > l:
                if(profit < prices[r]-prices[l]):
                    profit = prices[r]-prices[l]
                else:
                    r-=1
            l+=1
        return profit;

