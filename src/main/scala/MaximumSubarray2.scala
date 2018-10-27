object MaximumSubarray2 extends App{
  def maxSubArray(nums: Array[Int]): Int = {
      if(nums.isEmpty) 0
      else {
         var maxSum = Int.MinValue
         var sumSub = Int.MinValue
         for(i <- 0 to nums.length-1) {
           if(sumSub == Int.MinValue)
             sumSub = nums(i)
           else
              sumSub = nums(i) max (sumSub + nums(i))
           maxSum = sumSub max maxSum
         }
         maxSum
      }
  }
  println(maxSubArray(Array(-1)))
  println(maxSubArray(Array(-2,1,-3,4,-1,2,1,-5,4)))

}
