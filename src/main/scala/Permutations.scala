import scala.collection.mutable.ListBuffer

object Permutations extends App {
  def perm(arr:Array[Int]): List[List[Int]] = {
    val result = new ListBuffer[List[Int]]()
    generate(arr, Array.ofDim[Boolean](arr.length), result, List.empty)
    result.toList
  }

  private def generate(s: Array[Int],  chosen:Array[Boolean], res: ListBuffer[List[Int]], buf: List[Int]):Unit = {
    if(buf.size == s.length) res += buf
    else {
      for(i <- 0 to s.length - 1) {
        if(!chosen(i)){
          val perm = buf :+ s(i)
          chosen(i) = true
          generate(s, chosen, res, perm)
          chosen(i) = false
        }
      }
    }
  }

   val arr = Array(1,2,3)
   val res = perm(arr)
   res.foreach(l => println(l.mkString(",")))

}
