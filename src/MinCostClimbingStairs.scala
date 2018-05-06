package leetcode

object MinCostClimbingStairs extends App {
  private def minCostClimbingStairs(mem: collection.mutable.Map[Int, Int], cost: Array[Int], from: Int): Int = {
    if(from >= cost.length) 0
    else
    if(mem.contains(from)) mem(from)
    else{
      val sum = cost(from) + (minCostClimbingStairs(mem, cost, from + 1) min minCostClimbingStairs(mem, cost, from + 2))
      mem += (from -> sum)
      sum
    }
  }

  def minCostClimbingStairs(cost: Array[Int]): Int = {
    //val mem = collection.mutable.Map[Int,Int]()
    //minCostClimbingStairs(mem, cost, 0) min minCostClimbingStairs(mem, cost, 1)
    var f1 = 0
    var f2 = 0
    for(i <- cost.length - 1 to 0 by -1) {
       val f0 = cost(i) + (f1 min f2)
       f2 = f1
       f1 = f0
    }
    f1 min f2
  }

  var arr1 = Array(10, 15, 20)
  println(minCostClimbingStairs(arr1))

  val arr2 = Array(1, 100, 1, 1, 1, 100, 1, 1, 100, 1)
  println(minCostClimbingStairs(arr2))
}
