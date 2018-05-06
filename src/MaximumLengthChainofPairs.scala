package leetcode

object MaximumLengthChainofPairs extends App {
  def maxLength(pairs: Array[(Int, Int)]): Int = {
    if(pairs.isEmpty) 0
    else {
      val spairs = pairs.sortBy(_._1)
      maxChainLen(spairs)
    }
  }

  //index of min pair and len
  private def findMin(pairs: Array[(Int, Int)], from: Int): (Int, Int) = {
    if(pairs.isEmpty) (0, 0)
    else
    if (from == pairs.length - 1) (from, 1)
    else {
      val (minInd, len1) = findMin(pairs, from + 1)
      val a = pairs(from)
      val b = pairs(minInd)
      if (a._2 < b._1) (from, len1 + 1)
      else (minInd, len1)
    }
  }

  //pairs is sorted
  def maxChainLen(pairs: Array[(Int, Int)]):Int = {
     val mlc = Array.fill[Int](pairs.length)(1)
     for(i <- 0 until pairs.length){
        for(j <- 0 until i) {
           if(pairs(i)._1 > pairs(j)._2 && mlc(i) < mlc(j) + 1) mlc(i) = mlc(j) + 1
        }
     }
     mlc.max
  }

  val arr1 = Array((5, 24), (39, 60), (15, 28), (27, 40), (50, 90))
  println(maxLength(arr1))

  println(maxLength(Array.empty[(Int,Int)]))

  val arr2 = Array((1,0))
  println(maxLength(arr2))
}
