package leetcode

object FindAllNumbersDisappearedArray extends App {
  def findDisappearedNumbers(nums: Array[Int]): List[Int] = {
    var list = List.empty[Int]
    for(i <- 0 until nums.size) {
      val ind = Math.abs(nums(i)) - 1
      if (nums(ind) > 0) {
        nums(ind) = -nums(ind)
      }
    }
    for(i <- (nums.size - 1) to 0 by -1) {
      if (nums(i) > 0) list = (i + 1) :: list
    }
    list
  }

  val array = Array(4, 3, 2, 7, 8, 2, 3, 1)

  println(findDisappearedNumbers(array))
}
