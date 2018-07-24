object FindDuplicateNumber extends App {
  def findDuplicate(nums: Array[Int]): Int = {
    if (nums == null || nums.isEmpty) -1
    else {
      val sorted = nums.sorted
      for(i <- 1 to sorted.length - 1){
         if(sorted(i-1) == sorted(i)) return sorted(i)
      }
      -1
    }
  }

  val arr4 = Array(21,1,27,1,1,17,10,1,33,1,37,1,1,1,31,40,1,39,1,1,1,1,1,1,32,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,15,1,1,1,1,8,25,49,1)
  println(findDuplicate(arr4))

  val arr3 = Array(13,17,11,18,9,19,15,7,14,3,16,15,15,15,15,10,2,6,12,15)
  println(findDuplicate(arr3))

  val arr1 = Array(14,16,12,1,16,17,6,8,5,19,16,13,16,3,11,16,4,16,9,7)
  println(findDuplicate(arr1))

  val arr2 = Array(1,3,4,2,2)
  println(findDuplicate(arr2))
}
