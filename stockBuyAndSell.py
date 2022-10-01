'''
Approach 1 -> For each day find the max price you can sell stock at and calculate maxProfit(i) for the day
maxProfit = max(maxProfit, maxProfit(i)) for i <- [0, n - 1]
T.C. -> O(n^2) and SC -> O(1)

Approach 2 -> Using stack find the maxValue to the right of each element then use that to find maxProfit(ith day)
TC -> O(n) SC-> O(n)

(BEST)Approach 3 -> To get maxProfit we need to sell the stock at min Possible price
so if possible to buy at smaller price then do and it will maximize the profit
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        buyPrice = float('inf')
        for curPrice in prices:
            # buy at lower price if possible
            if curPrice < buyPrice:
                buyPrice = curPrice
            maxProfit = max(maxProfit, curPrice - buyPrice)   
        return maxProfit
        