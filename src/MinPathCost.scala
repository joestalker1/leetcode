object MinPathCost extends App {
  def minCost(cost: Array[Array[Int]], m: Int, n: Int): Int = {
    if (m == 0 && n == 0) cost(m)(n)
    else if (m == 0) minCost(cost, m, n - 1) + cost(0)(n)
    else if (n == 0) minCost(cost, m - 1, n) + cost(m)(0)
    else {
      val x = minCost(cost, m - 1, n)
      val y = minCost(cost, m, n - 1)
      (x min y) + cost(m)(n)
    }
  }
}
