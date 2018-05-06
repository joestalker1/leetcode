package leetcode

object ContainsDuplicate2 extends App {
  def containsNearbyDuplicate(nums: Array[Int], k: Int): Boolean = {
    if(nums.length == 0) false
    else {
      val indices = nums.zipWithIndex.sortBy(_._1).map(_._2)
      var i = 0
      var repeated = false
      while(i < indices.length - 1 && !repeated){
        if(nums(indices(i)) == nums(indices(i + 1))
          && Math.abs(indices(i + 1) - indices(i)) <= k) repeated = true
        i += 1
      }
      repeated
    }
  }

  println(containsNearbyDuplicate(Array(2,2), 3))
}
