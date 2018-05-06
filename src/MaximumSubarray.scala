package leetcode

/**
  * Created by jstalker on 15.07.17.
  */
object MaximumSubarray extends App {
  private[this] case class MaxArray(lo:Int,hi:Int, sum: Int)
  def maxSubArray(nums: Array[Int]): Int = {

     def maxCrossingSubarray(arr: Array[Int],low: Int,mid: Int, hi:Int): MaxArray = {
        var lo_left = 0
        var sum = 0
        var lsum = Int.MinValue
        for(i <- mid to low by -1){
           sum += arr(i)
           if(sum > lsum){
              lsum = sum
              lo_left = i
           }
        }
        sum = 0
        var hi_left = 0
        var rsum = Int.MinValue
        for(i <- mid + 1 to hi){
         sum += arr(i)
         if(sum > rsum){
           rsum = sum
           hi_left = i
         }
       }
       MaxArray(lo_left, hi_left, rsum + lsum)
     }

     def maxSubarray(arr: Array[Int], lo:Int, hi:Int):MaxArray = {
       if(lo == hi) MaxArray(lo,hi, arr(lo))
       else {
         val mid = (lo + hi) / 2
         val MaxArray(lo_left,hi_left,left_sum) = maxSubarray(arr, lo, mid)
         val MaxArray(mid_left, mid_right, mid_sum) = maxCrossingSubarray(arr, lo, mid, hi)
         val MaxArray(lo_right, hi_right, right_sum) = maxSubarray(arr, mid + 1, hi)
         if(left_sum >= mid_sum && left_sum >= right_sum) MaxArray(lo_left,hi_left,left_sum)
         else if(right_sum >= left_sum && right_sum >= mid_sum) MaxArray(lo_right, hi_right, right_sum)
         else MaxArray(mid_left, mid_right, mid_sum)
       }

     }
     val MaxArray(_, _, sum) = maxSubarray(nums, 0, nums.size - 1)
     sum
  }

  //println(maxSubArray(Array(-2,1,-3,4,-1,2,1,-5,4)))
  println(maxSubArray(Array(-1,-1,-2,-2)))
}
