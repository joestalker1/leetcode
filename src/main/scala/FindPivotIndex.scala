package leetcode

object FindPivotIndex extends App {
  def pivotIndex(nums: Array[Int]): Int = {
    val sum = nums.sum
    var i = 0
    var left = 0
    var pivot = -1
    while (i <= nums.length && pivot == -1) {
      if ((sum - left - nums(i)) == left) pivot = i
      left += nums(i)
      i += 1
    }
    pivot
  }

  val arr1 = Array(-1, -1, -1, -1, -1, 0)
  //println(pivotIndex(arr1))

  val arr2 = Array(-1, -1, -1, -1, 0, -1)
  println(pivotIndex(arr2))

}
