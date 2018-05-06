package leetcode

object ReshapeMatrix extends App {
  def matrixReshape(nums: Array[Array[Int]], r: Int, c: Int): Array[Array[Int]] = {
     val totalSize = nums.foldRight(0){(arr, total) =>
       total + arr.size
     }
     val rows = totalSize / c
     if(totalSize % c != 0 || rows != r) nums
     else {
       val arr = Array.ofDim[Int](r, c)
       val allArr = nums.foldLeft(List.empty[Int]){(list, arr) =>
         list ++ arr
       }
       for{
         i <- 0 until r
         j <- 0 until c
       } {
         arr(i)(j) = allArr(i * c + j)
       }
       arr
     }
  }

  val arr = Array(Array(1,2),Array(3,4))
  println(matrixReshape(arr, 1, 4).map(_.mkString(",")).mkString("\r\n"))
}
