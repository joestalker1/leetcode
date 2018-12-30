import scala.collection.mutable.HashMap

object CoinChange extends App {
  def coinChange(coins: Array[Int], amount: Int): Int = {
    if(coins.isEmpty || amount < 0 || coins.min > amount && amount > 0) -1
    else {
      val minWays = new HashMap[Int,Int]
      minWays += (0 -> 0)
      val minCoin = coins.min
      if(minCoin <= amount) minWays += (minCoin -> 1)
      var a = minCoin + 1
      while(a <= amount) {
        for(coin <- coins) {
           if(a - coin >= 0 && minWays.contains(a - coin)){
             val ways = 1 + minWays(a - coin)
             val old = minWays.get(a)
             old.filter(_ > ways)foreach{_ =>
               minWays += (a -> ways)
             }
             old.getOrElse{
               minWays += (a -> ways)
             }
           }
        }
        a += 1
      }
      minWays.getOrElseUpdate(amount, -1)
    }
  }
  println(coinChange(Array(2), 0))
  println(coinChange(Array(474,83,404,3),264))
}
