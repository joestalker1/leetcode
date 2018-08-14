package leetcode

import scala.collection.mutable.ListBuffer
import scala.io.Source

object LongestContinuousIncreasingSubsequence extends App {
  def findLengthOfLCIS(nums: Array[Int]): Int = {
    if (nums.length <= 1) nums.length
    else {
      var maxr = 0
      var len = 1
      var j = 1
      while (j < nums.length) {
        if (nums(j - 1) < nums(j)) {
          len += 1
        } else {
          //reset i1 and i2
          maxr = len max maxr
          len = 1
        }
        j += 1

      }
      maxr max len
    }
  }

  val arr1 = Array(2, 2, 2, 2, 2)
  assert(findLengthOfLCIS(arr1) == 1)

  val arr2 = Array(10, 9, 8, 7, 5)
  assert(findLengthOfLCIS(arr2) == 1)

  val arr3 = Array(1, 3, 5, 4, 7)
  assert(findLengthOfLCIS(arr3) == 3)

  val arr4 = Array(-1, 2, -3, 4, 4, -1, 2, -3, 4, 4, -1, 2, -3, 4, 4)
  assert(findLengthOfLCIS(arr4) == 2)
  val buffer = new ListBuffer[Int]()
  Source.fromFile("/home/jstalker/long_array.txt").getLines().foldLeft(buffer){(sb, s)=>
    val parts = s.split(",")
    buffer ++= parts.map(_.toInt)
    buffer
  }
  val arr5 = buffer.toArray
  println(findLengthOfLCIS(arr5))

}
