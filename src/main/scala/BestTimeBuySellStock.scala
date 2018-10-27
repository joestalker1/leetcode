object BestTimeBuySellStock  extends App {
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
          maxprofit = (prices(i) - minprice) max maxprofit
        }
      }
      maxprofit
    }

  }

  println(maxProfit(Array(2, 4, 1)))
  println(maxProfit(Array(2,1)))
  println(maxProfit(Array(7,6,4,3,1)))
  println(maxProfit(Array(7,1,5,3,6,4)))

}
