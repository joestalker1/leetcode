object PaintFence extends App {
  def numWays(n: Int, k: Int): Int = {
     val dp = Array(0, k, k * k, 0)
     if(n <= 2) dp(n)
     else{
       for(_ <- 3 to n){
          dp(3) = (k-1)*(dp(1) + dp(2))
          dp(1) = dp(2)
          dp(2) = dp(3)
       }
       dp(3)
     }
  }
  println(numWays(2, 4))
}
