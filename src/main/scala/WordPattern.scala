package leetcode

import scala.io.StdIn

object WordPattern extends App {
  def wordPattern(pattern: String, str: String): Boolean = {
    if (pattern.isEmpty && str.isEmpty) true
    else {
      val words = str.split(" ")
      if (pattern.length != words.length) false
      else {
        var map1 = Map.empty[Char, String]
        var map2 = Map.empty[String, Char]
        var i = 0
        var f = true
        while (i < pattern.length && f) {
          val c = pattern(i)
          val word = words(i)
          val ifContainChar = map2.get(word)
          if (ifContainChar.filter(_ != c).nonEmpty) f = false
          else if (ifContainChar.isEmpty) {
            val ifContainWord = map1.get(c)
            if (ifContainWord.filter(_ != word).nonEmpty) f = false
            else{
              map1 = map1 + (c -> word)
              map2 = map2 + (word -> c)
            }

          }
          i += 1
        }
        f
      }
    }
  }

  val s1 = "abba"
  val t1 = "dog cat cat dog"
  println(wordPattern(s1, t1))

  val s2 = "abba"
  val t2 = "dog cat cat fish"
  println(wordPattern(s2, t2))

  val s3 = "aaaa"
  val t3 = "dog cat cat dog"
  println(wordPattern(s3, t3))

  val s4 = "abba"
  val t4 = "dog dog dog dog"
  println(wordPattern(s4, t4))

}
