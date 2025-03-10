class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = float('inf')
        currentMax = float('-inf')
        profit = 0

        for n in prices:
            if n < currentMin:
                currentMin = n
                currentMax = currentMin # resets currentMax to currentMin in order to find only max profit starting from this day and beyond
            elif n > currentMax:
                currentMax = n
                profit = max(profit, currentMax - currentMin)
        return profit