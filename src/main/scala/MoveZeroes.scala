package leetcode

object MoveZeroes extends App {
  def moveZeroes(nums: Array[Int]): Unit = {
     var i = 0 //0 cursor
     var j = 0
     while(i < nums.size && j < nums.size){
       while(i < nums.size && nums(i) != 0) i += 1
       while(j < nums.size && nums(j) == 0) j += 1

       if(i < j && i < nums.size && j < nums.size) {
         nums(i) = nums(j)
         nums(j) = 0
       } else {
         j += 1
       }
     }
  }
  val arr = Array(0, 1)
  moveZeroes(arr)
  println(arr.mkString(","))

}
