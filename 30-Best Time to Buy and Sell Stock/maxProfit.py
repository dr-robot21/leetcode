from typing import List


def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if n == 0 : return 0
    min_p , profit = 0 , 0 
    for i in range(n):
        if prices[min_p] > prices[i]:
            min_p = i
        profit = max(profit,prices[i] - prices[min_p])
    return profit
