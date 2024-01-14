class Solution {
    fun maxProfit(prices: IntArray): Int {
        // buying stock should be the min
        // selling stock should be the max
        // iterate through array keeping track of selling stock
        // if an element is greater than buying stock keep track of difference
        var buyingStock = prices[0]
        var profit = 0
        prices.forEach { p -> 
            if (p < buyingStock) buyingStock = p
            else {
                profit = max(profit, p - buyingStock)
            }
        }

        return profit
    }
}