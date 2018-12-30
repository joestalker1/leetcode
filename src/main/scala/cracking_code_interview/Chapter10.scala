package cracking_code_interview

import scala.collection.mutable.ListBuffer

object Task10_1 extends App {
  def sort(a:Array[Int], b:Array[Int]):Array[Int] = {
     if(a.length > b.length) Array.empty[Int]
     else {
       var i = a.length - 1
       while(i >= 0 && a(i) == Int.MinValue) i-= 1
       i = a.length - i - 1
       var j = i
       a.copyToArray(a, i)
       i = 0
       var k = 0
       while(k < b.length) {
         if(a(j) < b(i)) {
           a(k) = a(j)
           j += 1
         } else if(a(j) >= b(i)){
           a(k) = b(i)
           i += 1
         }
         k += 1
       }
       a
     }
  }
}
//177,182,263,342
object Task10_2 extends App {
   private def xorString(s:String):Int = {
     var xor = 0
     for(ch <- s) xor = xor ^ ch
     xor
   }

   def groupAnagrams(words:Array[String]):Array[String] = {
      if(words.isEmpty) Array.empty[String]
      else {
        words.sortWith{(s1,s2) =>
          s1.toSet == s2.toSet
        }
      }
   }

   println(groupAnagrams(Array("abcd"," wewewe","wevvvvv","dcba")).mkString(","))
 }

object Task10_3 extends App {

}

class Listy(arr: IndexedSeq[Int]) {
  private val posToElement: Map[Int,Int] = arr.zipWithIndex.map{case (a:Int,i: Int) => (i -> a)}.toMap

  def elementAt(i: Int):Int = posToElement.getOrElse(i, -1)

}


object Task10_4 extends App {

  def search(l:Listy, x:Int):Option[Int] = {
      var i = 0
      var j = 2
      var  stop = false
      while(!stop) {
        val a = l.elementAt(i)
        val b = l.elementAt(j)
        if(a == -1 && b == -1) return None
        if(x >= a && x <= b) stop = true
        else {
          i = j
          j = j * 2
        }
      }
      //implement binary search for [i,j]
      while(i <= j){
        val mid = i + (j -i) / 2
        if(l.elementAt(mid) == x) return Some(mid)
        else if(l.elementAt(mid) > x) j = mid - 1
        else i = mid + 1
      }
      None
  }
}
//235, 254, 281
object Task10_7 extends App {
}
//289, 315

class MyBitSet() {
  private var buf = Array.ofDim[Long](16)

  def +=(a: Int):Unit = {
    //Long is 64 bits length
    val i = a / 64
    //allocate new array if it's not enough room
    if(i >= buf.length) {
       var len = buf.length
       while(len <= i) len <<= 1
       val newBuf = Array.ofDim[Long](len)
       buf.copyToArray(newBuf)
       buf = newBuf
    }
    val j = 1 << (a % 64)
    buf(i) |= j
  }

  def has(a: Int):Boolean = {
     val i = a / 64
     if(i >= buf.length) false
     else (buf(i) & ( 1 << (a % 64))) != 0
  }
}

object Task10_8 extends App {
  def findDuplicate(nums:Array[Int]):List[Int] = {
     val bitSet = new MyBitSet()
     val dups = new ListBuffer[Int]()
     for(a <- nums){
       if(bitSet.has(a)) dups += a
       else bitSet += a
     }
     dups.toList
  }

  println(findDuplicate(Array(1,2,3,1,2)).mkString(","))
}
//193, 211, 229, 251, 266, 279, 288, 291, 303, 317,330
object Task10_9_1 extends App {

}
//301, 376, 392
object Task10_10 extends App {
   def rankFromStream():Unit = () // use search binary tree
}

//196,219,231,253,277,292,316
object Task10_11 extends App {

}