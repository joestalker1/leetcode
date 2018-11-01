
import scala.collection.mutable.ListBuffer

object GeneratePermutations extends App {
   def search(perm:ListBuffer[Int],seen:Array[Boolean], n:Int):Unit = {
      if(perm.length == n){
        println(perm.toList.mkString(","))
      } else {
         for(i <- 0 until n if !seen(i)){
             seen(i) = true
             perm.append(i)
             search(perm, seen, n)
             seen(i) = false
             perm.remove(perm.length - 1)
         }
      }
   }
   search(new ListBuffer[Int](),Array.ofDim[Boolean](4), 4)
}
