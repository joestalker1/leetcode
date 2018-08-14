object PaintHouse extends App {
  def minCost(costs: Array[Array[Int]]): Int = {
    if (costs.isEmpty) 0
    else {
      for (i <- 1 until costs.length) {
        costs(i)(0) += costs(i - 1)(1) min costs(i - 1)(2)
        costs(i)(1) += costs(i - 1)(0) min costs(i - 1)(2)
        costs(i)(2) += costs(i - 1)(0) min costs(i - 1)(1)
      }
      costs(costs.length - 1)(0) min costs(costs.length - 1)(1) min costs(costs.length - 1)(2)
    }
  }

  val costs = Array(
    Array(1, 3, 44),
    Array(10, 2, 3),
    Array(23, 3, 4),
    Array(23, 33, 4),
    Array(23, 3, 34),
    Array(2, 3, 4)
  )
  println(minCost(Array.empty))
}
