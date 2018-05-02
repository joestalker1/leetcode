object ClimbingStairs extends App {
  def climbStairs(n: Int): Int = {
    val dp = Array.ofDim[Int](n + 1)
    dp(1) = 1
    dp(2) = 2
    for (i <- 3 to n) {
      dp(i) = dp(i - 1) + dp(i - 2)
    }
    dp(n)
  }

  println(climbStairs(45))
  println(climbStairs(3))
  println(climbStairs(2))
}
