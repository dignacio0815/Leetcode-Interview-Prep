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












        /*
        // outer loop i = 0 until prices.size - 1
        //      buy = -prices[i]
        //      nested loop j = i + 1 ..
        //          sell = prices[j]
        //          profit = buy + sell
        //          if (profit < negative) {}
        //          elif (profit > positive) {
                        finalProfit = profit
                    }
         */
        // loop over prices i = 1
        /*
            if (sellingPrice - buyingPrice > 0) {
                finalProfit = max(sellingPrice - buyingPrice, finalProfit)
            }
            if (prices[i] < buyingPrice) {
                buyingPrice = min(buyingPrice, prices[i])
            } else if (prices[i] > buyingPrice) {
                sellingPrice = max(sellingPrice, prices[i])
            }

        return profit
         */

    
        


        //  for (i in 0 until prices.size - 1) {
        //      // buying here so implies negative - losing money
        //      buy = -prices[i]
        //      for (j in i + 1 until prices.size) {
        //         // selling here implies positive - gains
        //         sell = prices[j]
        //         var temp = buy + sell
        //         println("sell: $sell, buy: $buy profit $temp")
        //         if (temp > 0) {
        //             finalProfit = max(temp, finalProfit)
        //         }
        //      }
        //  }
    }
}