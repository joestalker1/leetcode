package leetcode

/**
  * Created by jstalker on 09.07.17.
  */
object RemoveDuplicatesSortedArray extends App {
  def removeDuplicates(nums: Array[Int]): Int = {
    var len = nums.length
    var j = 0
    for (i <- 0 until nums.length) {
      if (i > 0 && nums(i) == nums(i - 1)) {
        if(j == 0) j = i
        len -= 1
      } else if (i > 0 && nums(i) != nums(i - 1) && j > 0) {
        nums(j) = nums(i)
        j += 1
      }
    }
    len
  }

  val arr1 = Array(1, 1, 2)
  println(removeDuplicates(arr1))
  println(arr1.mkString(","))

  val arr2 = Array(1, 1)
  println(removeDuplicates(arr2))
  println(arr2.mkString(","))

  val arr3 = Array(1, 1, 1, 2)
  println(removeDuplicates(arr3))
  println(arr3.mkString(","))

}
