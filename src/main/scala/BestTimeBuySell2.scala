package leetcode

object BestTimeBuySell2 extends App {
  def maxProfit(prices: Array[Int]): Int = {
    if (prices.isEmpty) 0
    else {
      var maxprofit = 0
      var minprice = Int.MaxValue
      for (i <- 0 to prices.length - 1) {
        if (minprice > prices(i)) {
          minprice = prices(i)
        }
        else if ((prices(i) - minprice) > 0) {
          maxprofit += prices(i) - minprice
          minprice = prices(i)
        }
      }
      maxprofit
    }
  }
  println(maxProfit(Array(1,2,4)))
}
