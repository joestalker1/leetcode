
object SolutionApp extends App {

  // 1 int is lo,second is hi, 3 is sum
  private def maxCrossingSubarray(arr: Array[Int], low: Int, mid: Int, hi: Int): (Int,Int,Int) = {
    var lo_left = 0
    var sum = 0
    var lsum = Int.MinValue
    for (i <- mid to low by -1) {
      sum += arr(i)
      if (sum > lsum) {
        lsum = sum
        lo_left = i
      }
    }
    sum = 0
    var hi_left = 0
    var rsum = Int.MinValue
    for (i <- mid + 1 to hi) {
      sum += arr(i)
      if (sum > rsum) {
        rsum = sum
        hi_left = i
      }
    }
    (lo_left, hi_left, rsum + lsum)
  }

  private def maxSubarray(arr: Array[Int], lo: Int, hi: Int): (Int,Int,Int) = {
    if(arr.length == 0) (0, 0, 0)
    else
    if (lo >= hi) (lo, hi, arr(lo))
    else {
      val mid = (lo + hi) / 2
      val (lo_left, hi_left, left_sum) = maxSubarray(arr, lo, mid)
      val (mid_left, mid_right, mid_sum) = maxCrossingSubarray(arr, lo, mid, hi)
      val (lo_right, hi_right, right_sum) = maxSubarray(arr, mid + 1, hi)
      if (left_sum >= mid_sum && left_sum >= right_sum) (lo_left, hi_left, left_sum)
      else if (right_sum >= left_sum && right_sum >= mid_sum) (lo_right, hi_right, right_sum)
      else (mid_left, mid_right, mid_sum)
    }

  }

  def maxProfit(prices: Array[Int]): Int = {
    for(i <- prices.length - 1 to 0 by -1 ) {
      prices(i) = if(i == 0) 0 else prices(i) - prices(i-1)
    }
    val (_, _, sum) = maxSubarray(prices, 0, prices.size - 1)
    sum
  }

  println(maxProfit(Array()))
}

