object ClimbingStairs extends App {
  def climbStairs(n: Int): Int = {
    if (n <= 0) 0
    else if(n == 1 || n == 2) n
    else {
      val ways = Array.ofDim[Int](n + 1)
      ways(1) = 1
      ways(2) = 2
      for (i <- 3 to n) {
        ways(i) = ways(i - 1) + ways(i - 2)
      }
      ways(n)
    }
  }
  println(climbStairs(45))
  println(climbStairs(3))
  //println(climbStairs(2))
}
