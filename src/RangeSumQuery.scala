class RangeSumQuery(_nums:Array[Int]) {
  def sumRange(i: Int, j: Int): Int = {
     val sum = Array.ofDim[Int](_nums.length)
     sum(0) = _nums(0)
     for(i <- 1 until sum.length) {
       sum(i) = sum(i - 1) + _nums(i)
     }
     sum(j) - sum(i) + _nums(i)
  }
}

object RangeSumQueryApp extends App {
  val rsq = new RangeSumQuery(Array(-2, 0, 3, -5, 2, -1))
  println(rsq.sumRange(0, 2))
  println(rsq.sumRange(2, 5))
}