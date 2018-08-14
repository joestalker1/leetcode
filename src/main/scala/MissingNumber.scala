package leetcode

object MissingNumber extends App {
  def missingNumber(nums: Array[Int]): Int = {
    var sum = nums.length
    for (i <- 0 to nums.length-1){
      sum += (i - nums(i))
    }
    sum
  }


  println(missingNumber(Array(1, 2)))
}
