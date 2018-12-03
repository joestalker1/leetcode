package cracking_code_interview

import scala.collection.mutable.ListBuffer

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

object Task8_33 extends App {
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
  private def subsets(arr: Array[Int], nums: scala.collection.mutable.ListBuffer[Int], k: Int): Unit = {
    if (k == arr.length) {
      if (nums.nonEmpty) println(nums.mkString(","))
    } else {
      subsets(arr, nums, k + 1)
      nums.append(arr(k))
      subsets(arr, nums, k + 1)
      nums.remove(nums.length - 1)
    }
  }

  def subsets(arr: Array[Int]): Unit = {
    subsets(arr, new scala.collection.mutable.ListBuffer[Int](), 0)
  }

  subsets(Array(1, 2, 3))
}

// 144, 224, 250, 272, 318
object Task8_6 extends App {
  def towersOfHanoi(from: String, withA: String, to: String, n: Int): Unit = {
    if (n == 1) ()
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
  private def perm(s: String, word: ListBuffer[Char], seen: scala.collection.mutable.Set[Int]): Unit ={
      if(word.length == s.length){
        println(word.result().toString())
      } else {
         for(i <- 0 to s.length - 1){
           if(!seen(i)){
              seen += i
              word += s(i)
              perm(s, word, seen)
              word.remove(word.length - 1)
              seen -= i
           }
         }
      }
  }

  def perm(s: String): Unit = {
      perm(s, new ListBuffer[Char](), scala.collection.mutable.Set[Int]())
  }

  perm("1234")
}

//#161, 190, 222, 255
object Task8_8 extends App {

}
//138,174,187,209, 243, 265,295
object Task8_9 extends App {
   private def printParens(num: Int,left:Int,right:Int,buf: Array[Char]):Unit = {
      if(left == 0 && right == 0){
         println(buf.mkString(""))
      } else {
         val pos = num - left - right
         if(left > 0){
           buf(pos) = '('
           printParens(num, left - 1, right, buf)
         }
         if(left < right) {
            buf(pos) = ')'
            printParens(num, left, right-1, buf)
         }
      }
   }
   def parens(n:Int):Unit = {
      val buf = Array.ofDim[Char](2*n)
      printParens(2 * n,n,n, buf)
   }

   parens(3)
}

object Task_8_11 extends App {
  private def ways(n:Int, w:Array[Int]):Int = {
     if(n <=0) 0
     else {
       if(w(n) != -1) {
         println(s"use table for $n ${w(n)}")
         w(n)
       }
       else {
         val a = 1 + ways(n - 25, w) + ways(n - 10, w) + ways(n - 5, w)
         w(n) = a
         println(s" for $n it equals $a")
         w(n)
       }
     }
  }

  def ways(n:Int):Int = {
    val w = Array.fill[Int](n + 1)(-1)
    w(0) = 0
    w(1) = 0
    w(2) = 0
    w(3) = 0
    w(4) = 0
    w(5) = 1
    ways(n, w)
  }

  println(ways(35))
}
//155,194,214,260,322,368,378
object Task8_13 extends App {

}
//148,168,197,305,327
object Task8_14 extends App {

}