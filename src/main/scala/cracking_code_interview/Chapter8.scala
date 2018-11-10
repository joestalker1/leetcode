package cracking_code_interview

object Task8_1 extends App {
  def tripleStep(n: Int): Int = {
    val ways = Array.ofDim[Int](n + 1)
    ways(1) = 1
    ways(2) = 2
    for (i <- 3 to n) {
      ways(i) = 1 + ways(i - 1) + ways(i - 2) + ways(i - 3)
    }
    ways(n)
  }

  println(tripleStep(7))
}

object Task8_3 extends App {
  def magicIndex(arr: Array[Int]): Option[Int] = {
    if (arr == null || arr.isEmpty) None
    else {
      var s = 0
      var e = arr.length - 1
      var res: Option[Int] = None
      while (s <= e && res.isEmpty) {
        val mid = s + (e - s) / 2
        if (arr(mid) == mid) res = Option(mid)
        else if (arr(mid) > mid) e = mid - 1
        else s = mid + 1
      }
      res
    }
  }

  println(magicIndex(Array(0, 2, 3, 4)))
}

object Task8_4 extends App {
   private def subsets(arr:Array[Int],nums: scala.collection.mutable.ListBuffer[Int], k: Int):Unit = {
      if(k == arr.length) {
        if(nums.nonEmpty) println(nums.mkString(","))
      } else {
        subsets(arr, nums, k + 1)
        nums.append(arr(k))
        subsets(arr, nums, k + 1)
        nums.remove(nums.length - 1)
      }
   }

   def subsets(arr:Array[Int]):Unit = {
       subsets(arr, new scala.collection.mutable.ListBuffer[Int](), 0)
   }

   subsets(Array(1, 2, 3))
}
// 144, 224, 250, 272, 318
object Task8_6 extends App {
   def towersOfHanoi(from:String, withA: String, to: String,n: Int):Unit = {
     if(n == 1) ()
     else {
       println(s"move a disk $from -> $to")
       println(s"move a disk $from -> $withA")
       println(s"move a disk $to -> $withA")
       println(s"move a disk $from -> $to")
       towersOfHanoi(withA, from, to, n - 1)
     }
   }

   println(towersOfHanoi("A", "B", "C", 2))
}

object Task8_7 extends App {

}