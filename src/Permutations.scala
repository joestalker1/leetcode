import scala.collection.mutable.ArrayBuffer

object Permutations extends App {
   def perm(arr:Array[Int]):List[List[Int]] = {
     val result = new ArrayBuffer[List[Int]]()
     compose(arr.toSet, result, Nil)
     result.toList
   }

   private def compose(n : Set[Int],result : ArrayBuffer[List[Int]], path: List[Int]): Unit = {
     if(n.isEmpty) result += path
     else{
       for(a <- n){
         val newPath = path :+ a
         compose(n - a, result, newPath)
       }
     }
   }

   val arr = Array(1,2,3)
   val res = perm(arr)
   res.foreach(l => println(l.mkString(",")))

}
