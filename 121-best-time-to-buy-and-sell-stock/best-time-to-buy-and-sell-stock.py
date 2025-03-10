class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = float('inf')
        currentMax = float('-inf')
        profit = 0

        for n in prices:
            if n < currentMin:
                currentMin = n # 0
                currentMax = currentMin
            elif n > currentMax:
                currentMax = n # 2
                print(f"current max is {currentMax}")
                profit = max(profit, currentMax - currentMin)
            # print(f"current max is {currentMax} and min is {currentMin} with n being {n}")
        return profit