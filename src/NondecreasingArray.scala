package leetcode


object NondecreasingArray extends App {

  def checkPossibility(nums: Array[Int]): Boolean = {
    val newA = nums.clone()
    var j = 0
    var f = false
    while (j < nums.length && !f) {
      val old = nums(j)
      newA(j) = if (j > 0) newA(j - 1) else Int.MinValue
      if (monotoneInscreasing(newA)) f = true
      else {
        newA(j) = old
      }
      j += 1
    }
    f
  }

  def monotoneInscreasing(arr: Array[Int]): Boolean = {
    var j = 0
    var incr = true
    while (j < arr.length && incr) {
      if (arr(j) > arr(j + 1)) incr = false
      j += 1
    }
    incr
  }

  //  val arr1 = Array(4, 2, 1)
  //  assert(checkPossibility(arr1) == false)
  //  val arr2 = Array(4, 2, 3)
  //  assert(checkPossibility(arr2))
  //  val arr3 = Array(3, 4, 2, 3)
  //  assert(checkPossibility(arr3) == false)
  //  val arr4 = Array(1, 2, 3)
  //  assert(checkPossibility(arr4))
  //  val arr5 = Array(1, 5, 4, 6, 7, 10, 8, 9)
  //  assert(checkPossibility(arr5)== false)
  //  val arr6 = Array(3, 3, 2, 2) //false
  //  assert(checkPossibility(arr6) == false)
  //  val arr7 = Array(2, 6, 4, 8, 10, 9, 15)
  //  assert(checkPossibility(arr7) == false)
  //  val arr8 = Array(1, 2, 5, 3, 3)
  //  assert(checkPossibility(arr8))
  //  val arr9 = Array(4, 2, 1)
  //  assert(checkPossibility(arr9)== false)
  //  val arr10 = Array(1,3,5,2,4)
  //  assert(checkPossibility(arr10)==false)
  //  val arr11 = Array(1)
  //  assert(checkPossibility(arr11))
  //  val arr12 = Array(2,3,3,2,4)
  //  assert(checkPossibility(arr12))
  //  val arr13 = Array(1,2,4,5,3)
  //  assert(checkPossibility(arr13))
  //  val arr14 = Array(-1,4,2,3)
  //  assert(checkPossibility(arr14))
  val arr15 = Array(2, 4, 1, 3, 5)
  assert(checkPossibility(arr15) == false)
}
