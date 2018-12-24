object NextPermutation extends App {
  private def reverse(nums:Array[Int], from:Int):Unit = {
    var i = from
    var j = nums.length - 1
    while(i < j){
      val t = nums(i)
      nums(i) = nums(j)
      nums(j) = t
      i += 1
      j -= 1
    }
  }

  def nextPermutation(nums: Array[Int]): Unit = {
    if(nums == null || nums.size == 0) ()
    else {
      var i = nums.length - 2
      while(i >= 0 && nums(i+1) <= nums(i)) i -= 1
      if(i >=0 ){
         var j = nums.length - 1
         while(j >= 0 && nums(j) <= nums(i)) j -= 1
         val t = nums(i)
         nums(i) = nums(j)
         nums(j) = t
      }
      reverse(nums, i + 1)
    }
  }

  val arr1 = Array(1,2,3)
  nextPermutation(arr1)
  println(arr1.mkString(","))

  val arr2 = Array(1,1,5)
  nextPermutation(arr2)
  println(arr2.mkString(","))

  val arr3 = Array(1,3,2)
  nextPermutation(arr3)
  println(arr3.mkString(",")) //2,1,3

}
