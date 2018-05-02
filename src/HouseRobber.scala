object HouseRobber extends App {
  def rob(nums: Array[Int]): Int = {
    if(nums.isEmpty) 0
    else if(nums.length == 1) nums(0)
    else if (nums.length == 2) nums.max
    else {
      val money = Array.ofDim[Int](nums.length + 1)
      money(1) = nums(0)
      for (i <- 2 to nums.length) {
        val loot = money(i - 1) max (money(i - 2) + nums(i - 1))
        money(i) = loot
      }
      money(nums.length)
    }
  }

  print(rob(Array(1,10,3,4)))

}
