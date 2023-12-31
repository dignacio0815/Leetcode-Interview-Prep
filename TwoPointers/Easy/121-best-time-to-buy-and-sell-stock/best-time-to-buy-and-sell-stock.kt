class Solution {
    fun maxProfit(prices: IntArray): Int {
        if (prices.size <= 1) return 0

        var buyingStock = prices[0]; var profit = 0

        for (i in 1 until prices.size) {
            if (prices[i] < buyingStock) {
                buyingStock = prices[i]
            } else if (prices[i] > buyingStock) {
                profit = max(abs(prices[i] - buyingStock), profit)
            }
        }
        
        return profit
    }
}