package leetcode

object RotateArray extends App {
  def rotate(nums: Array[Int], k: Int): Unit = {
    if(nums.size > 1){
      val nk = if(k > nums.size) k % nums.size else k
      val right = Array.ofDim[Int](nk)
      copyFrom(nums, right, nums.size - nk)
      for(i <- nums.size- nk - 1 to 0 by -1) {
        nums(i + nk) = nums(i)
      }
      copyFrom(right, nums, 0)
    }
  }

  private def copyFrom(arr:Array[Int],dest:Array[Int],from:Int):Unit = {
     var i = from
     var j = 0
     while(i < arr.size && j < dest.size){
        dest(j) = arr(i)
        j += 1
        i += 1
     }
  }
  var arr = Array(1,2,3)
  rotate(arr, 4)
  println(arr.mkString(","))
}
