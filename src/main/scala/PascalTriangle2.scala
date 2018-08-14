package leetcode

object PascalTriangle2 extends App {
  def getRow(rowIndex: Int): List[Int] = {
     if(rowIndex == 0) List(1)
     else {
       var buf = List(1)
       for(i <- 1 to rowIndex){
          var a = buf.head
          for(j <- 1 to i - 1){
            val sum = buf(j) + a
            a = buf(j)
            buf = buf :+ sum
          }
          buf = buf :+ 1
       }
       buf
     }
  }
  println(getRow(5))
}
