package leetcode

object KdiffPairsInArray extends App {
  def findPairs(nums: Array[Int], k: Int): Int = {
    val sorted = nums.sorted
    var count = 0
    for(i <- 0 until sorted.size - 1){
      if(i == 0 || sorted(i-1) != sorted(i)){
        var j = i + 1
        while(j < sorted.size) {
          val diff = math.abs(sorted(i) - sorted(j))
          if(diff == k && (j == (i+1) || (sorted(j-1) != sorted(j)))){
            count += 1
          }
          if(diff <= k && k > 0) j += 1
          else j = Int.MaxValue
        }
      }
    }
    count
  }

  val arr = Array(3, 1, 4, 1, 5)
  println(findPairs(arr, 2))

  val arr1 = Array(1, 3, 1, 5, 4)
  println(findPairs(arr1, 0))

  val arr2 = Array(1, 2, 3, 4, 5)
  println(findPairs(arr2, 1))

  val arr3 = Array(1, 1, 1, 2, 1)
  println(findPairs(arr3, 1))

  val arr4 = Array(1,1,1,1,1)
  println(findPairs(arr4, 0))

  val arr5 = Array(1,1,1,2,2)
  println(findPairs(arr5, 1)) //1
}
