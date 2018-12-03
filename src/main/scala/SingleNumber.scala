package leetcode

object SingleNumber extends App {
  def singleNumber(nums: Array[Int]): Int = {
    var x = 0
    for (i <- 0 until nums.length) {
      x = x ^ nums(i)
    }
    x
  }

  val arr1 = Array(2, 3, 2, 3, 1)
  println(singleNumber(arr1))
}
