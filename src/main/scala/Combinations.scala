import scala.collection.mutable.ListBuffer

object Combinations extends App {
   def comb(arr:Array[Int]): List[List[Int]] = {
       val result = new ListBuffer[List[Int]]()
       compose(0, arr, result, List.empty)
       result.toList
   }

   private def compose(i: Int, arr:Array[Int], result: ListBuffer[List[Int]], path: List[Int]): Unit = {
      if(i == arr.length){
         result += path
      } else {
        compose(i + 1,arr, result, path)
        val newPath = path :+ arr(i)
        compose(i + 1, arr, result, newPath)
      }
   }

   val arr = Array(1,2,3)
   val combinations = comb(arr)
   combinations.filter(_.nonEmpty).foreach( l => println(l.mkString(",")))
}
