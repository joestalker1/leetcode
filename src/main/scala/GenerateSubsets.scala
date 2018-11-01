import scala.collection.mutable.ListBuffer

object GenerateSubsets extends App {
   def search(k:Int, n:Int, buf: ListBuffer[Int]):Unit = {
      if(k == n){
        println(buf.toList.mkString(","))
      } else {
         search(k+1, n, buf)
         buf.append(k)
         search(k + 1, n, buf)
         buf.remove(buf.length - 1)
      }
   }

   search(0, 3, new ListBuffer[Int]())
}
