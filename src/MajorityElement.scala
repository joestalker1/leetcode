package leetcode

object MajorityElement extends App {
  private def findMajorityElement(nums: Array[Int]): Int = {
    var maj_i = 0
    var count = 1
    for(i <- 1 to nums.size - 1) {
       if(nums(i) == nums(maj_i)) count += 1
       else count = count - 1
       if(count == 0) {
         maj_i = i
         count = 1
       }
    }
    nums(maj_i)
  }

  private def isMajorElement(nums:Array[Int], a: Int): Boolean = {
     nums.count(_ == a) > nums.length / 2
  }

  def majorityElement(nums: Array[Int]):Int = {
    findMajorityElement(nums)
  }

  //println(majorityElement(Array(1, 2, 2, 2, 1)))
  println(majorityElement(Array(8,8,7,7,7)))
}
