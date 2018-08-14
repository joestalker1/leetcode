package leetcode

object ArrayPartition1 extends App {
  def arrayPairSum(nums: Array[Int]): Int = {
     val sorted = nums.sorted
     var i = 0
     var min1 = 0
     while(i < sorted.size){
       min1 += sorted(i)
       i+= 2
     }
     min1
  }
  val arr = Array(1,4,3,2)
  println(arrayPairSum(arr))
}
