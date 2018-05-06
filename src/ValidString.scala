package leetcode

import scala.io.StdIn

object ValidString extends App{
  def isAnagram(s: String, t: String): Boolean = {
     if(s.isEmpty && t.isEmpty) true
     else {
       var map = Map.empty[Char, Int]
       s.foreach{chr =>
         val c = map.getOrElse(chr, 0)
         map = map + (chr -> (c + 1))
       }
       var f = true
       var i = 0
       while(i < t.length && f){
         if(!map.contains(t(i))) f = false
         else {
           val c = map(t(i)) - 1
           if(c == 0) {
             map = map - t(i)
           } else map = map.updated(t(i), c)
         }
         i += 1
       }
       f && map.isEmpty
     }
  }
  val s = StdIn.readLine()
  val t = StdIn.readLine()
  println(isAnagram(s, t))
}
