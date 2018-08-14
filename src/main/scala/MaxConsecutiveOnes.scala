package leetcode

object MaxConsecutiveOnes extends App {
  def findMaxConsecutiveOnes(nums: Array[Int]): Int = {
    var len = 0
    var maxLen = 0
    for(i <- 0 until nums.size){
       if(nums(i) == 1) len += 1
       else {
         maxLen = len max maxLen
         len = 0
       }
    }
    maxLen max len
  }

  val arr = Array(1,1,0,1,1,1)
  println(findMaxConsecutiveOnes(arr))
}
