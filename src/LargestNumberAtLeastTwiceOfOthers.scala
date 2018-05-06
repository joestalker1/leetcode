package leetcode

object LargestNumberAtLeastTwiceOfOthers extends App {
  def dominantIndex(nums: Array[Int]): Int = {
     var mi = -1
     var max1 = Int.MinValue
     var max2 = Int.MinValue
     for(i <- 0 until nums.length){
       if(nums(i) > max1) {
         mi = i
         max2 = max1
         max1 = nums(i)
       } else if(nums(i) > max2) max2 = nums(i)
     }
    if((max2 * 2) > max1) -1 else mi
  }


  val arr1 = Array(1, 2, 3, 4)
  println(dominantIndex(arr1))

  val arr2 = Array(3, 6, 1, 0)
  println(dominantIndex(arr2))

  val arr3 = Array(0,0,3,2)
  println(dominantIndex(arr3))
}
