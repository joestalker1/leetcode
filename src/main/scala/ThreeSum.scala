import scala.collection.mutable.HashSet

object ThreeSum extends App {
  private def search(a: Int, nums: Array[Int],from: Int,to: Int):Option[Int] = {
    var i = from
    var j = to
    var res:Option[Int] = None
    while(i <= j && res.isEmpty){
      val mid = i + (j - i)/2
      if(nums(mid) == a) res = Some(mid)
      else if(nums(mid) > a) j = mid - 1
      else i = mid + 1
    }
    res
  }

  def threeSum(nums: Array[Int]): List[List[Int]] = {
     if(nums == null || nums.length < 3) List.empty
     else {
       val buf = new HashSet[List[Int]]()
       val sorted = nums.sorted
       for(i <- 0 to sorted.length - 3){
         val a = -sorted(i)
         for(j <- i + 1 to sorted.length - 2){
            val b = sorted(j)
            val c = a - b
            val res = search(c, sorted,j + 1, sorted.length - 1)
            res.foreach{k =>
               val newList = List(sorted(i), sorted(j), sorted(k))
               if(buf.isEmpty || !buf.contains(newList)) buf += newList
            }
         }
       }
       buf.toList
     }
  }

  val arr = Array(-1, 0, 1, 2, -1, -4)
  println(threeSum(arr).mkString(","))
}
