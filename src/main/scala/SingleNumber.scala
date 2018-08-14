package leetcode

object SingleNumber extends App {
  def singleNumber(nums: Array[Int]): Int = {
    var seen = Map.empty[Int, Int]
    for (i <- 0 until nums.length) {
      if (!seen.contains(nums(i))) seen = seen + (nums(i) -> 1)
      else seen = seen - nums(i)
    }
    seen.head._1
  }

  val arr1 = Array(2, 3, 2, 3, 1)
  println(singleNumber(arr1))
}
