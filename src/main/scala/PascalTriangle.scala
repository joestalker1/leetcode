package leetcode

object PascalTriangle extends App {
  def generate(numRows: Int): List[List[Int]] = {
    if(numRows == 0) List.empty
    if(numRows == 1) List(List(1))
    else
    if(numRows == 2) List(List(1), List(1,1))
    else {
      var triangle = List(List(1), List(1,1))
      for(i <- 2 to numRows){
         val mid = for(j <- 1 to triangle(i-1).size - 1) yield (triangle(i-1)(j-1) + triangle(i-1)(j))
         val nlist = (1 :: mid.toList) :+ 1
         triangle = triangle :+ nlist
      }
      triangle
    }
  }

  println(generate(5))
}
