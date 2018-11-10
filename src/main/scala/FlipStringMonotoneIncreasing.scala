object FlipStringMonotoneIncreasing extends App {
  private def countDiff(s: String, arr: Array[Byte]): Int = {
    var i = 0
    var count = 0
    while (i < arr.length) {
      val a = if (s(i) == '0') 0 else 1
      if (a != arr(i)) count += 1
      i += 1
    }
    count
  }

  private def isMonoIncr(arr: Array[Byte]): Boolean = {
    var i = 0
    var error = false
    while (i < arr.length && !error) {
      if (i > 0 && arr(i - 1) == 1 && arr(i) == 0) error = true
      i += 1
    }
    !error
  }

  def minFlipsMonoIncr(s: String): Int = {
    if (s == null || s.isEmpty) 0
    else {
      val arr = Array.ofDim[Byte](s.length)
      var k = arr.length-1
      var flips = countDiff(s, arr)
      while (k >= 0) {
        arr(k) = 1
        if (isMonoIncr(arr)) flips = flips min countDiff(s, arr)
        k -= 1
      }
      flips
    }
  }

  println(minFlipsMonoIncr("11011011010010110011"))
  println(minFlipsMonoIncr("11011"))
  println(minFlipsMonoIncr("00011000"))
  println(minFlipsMonoIncr("010110"))
  println(minFlipsMonoIncr("00110"))
}
