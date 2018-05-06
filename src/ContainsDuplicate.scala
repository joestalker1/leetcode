package leetcode

class ContainsDuplicate {
  def containsDuplicate(nums: Array[Int]): Boolean = {
     val sorted = nums.sorted
     var a = sorted(0)
     var j = 1
     var repeated = false
     while(j < sorted.size && !repeated){
        if(sorted(j) != a){
          a = sorted(j)
        } else repeated = true
        j += 1
     }
     repeated
  }

}
