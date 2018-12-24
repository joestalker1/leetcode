import scala.collection.mutable.ListBuffer

object SpiralMatrix extends App {
  private def move(matrix: Array[Array[Int]], upperLeft: (Int, Int), lowRight: (Int, Int), buf: ListBuffer[Int]): Unit = {
    var i = upperLeft._1
    var j = upperLeft._2
    val n = lowRight._1 - upperLeft._1 + 1
    val m = lowRight._2 - upperLeft._2 + 1
    while (j <= lowRight._2) {
      buf.append(matrix(i)(j))
      j += 1
    }
    j -= 1
    i += 1
    while (n > 1 && i <= lowRight._1) {
      buf.append(matrix(i)(j))
      i += 1
    }
    i -= 1
    j -= 1
    while (m > 1 && n > 1&& j >= upperLeft._2) {
      buf.append(matrix(i)(j))
      j -= 1
    }
    j += 1
    i -= 1
    while (n > 1 && m > 1&& i >= upperLeft._1 + 1) {
      buf.append(matrix(i)(j))
      i -= 1
    }
  }

  def spiralOrder(matrix: Array[Array[Int]]): List[Int] = {
    if (matrix == null || matrix.isEmpty) List.empty
    else {
      var r1 = 0
      var c1 = 0
      var r2 = matrix.length - 1
      var c2 = matrix(0).length - 1
      val buf = new ListBuffer[Int]()
      while (r1 <= r2 && c1 <= c2) {
        move(matrix, (r1, c1), (r2, c2), buf)
        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1
      }
      buf.toList
    }
  }
  val arr0 = Array(
    Array(7),
    Array(9),
    Array(6)
  )
  println(spiralOrder(arr0).mkString(","))
//
//  val arr = Array(
//    Array(1, 2, 3, 4),
//    Array(5, 6, 7, 8),
//    Array(9, 10, 11, 12)
//  )
//  println(spiralOrder(arr).mkString(","))
  //  val arr1 = Array(
  //    Array( 1, 2, 3 ),
  //    Array(4, 5, 6),
  //    Array( 7, 8, 9)
  //  )
  //  println(spiralOrder(arr1).mkString(","))
  //
  //  val arr2 = Array(
  //    Array(1, 2, 3, 4),
  //    Array(5, 6, 7, 8),
  //    Array(9,10,11,12)
  //  )
  //  println(spiralOrder(arr2).mkString(","))
}
