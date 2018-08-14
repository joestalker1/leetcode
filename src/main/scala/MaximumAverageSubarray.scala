package leetcode

object MaximumAverageSubarray extends App {
  def findMaxAverage(nums: Array[Int], k: Int): Double = {
    if(nums.size < k) 0
    else {
      var sum = nums.view(0, k).sum
      var max1 = sum
      var j = 1
      while((j + k) <= nums.size) {
        sum -= nums(j - 1)
        sum += nums(j + k - 1)
        if(max1 < sum) max1 = sum
        j += 1
      }
      (max1).toDouble / k.toDouble
    }
  }
  val arr = Array(1,12,-5,-6,50,3)
  val arr1 = Array(0,1,1,3,3)
  println(findMaxAverage(arr1, 4))
}
