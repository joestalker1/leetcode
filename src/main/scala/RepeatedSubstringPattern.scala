package leetcode

object RepeatedSubstringPattern extends App {
  def repeatedSubstringPattern(s: String): Boolean = {
    val double = s+s
    double.substring(1, double.length-1).indexOf(s) != -1
  }

  val s0 = "ababab"
  println(repeatedSubstringPattern(s0))

  val s1 = "aabaaba"
  println(repeatedSubstringPattern(s1))
  val s2 = "aba"
  println(repeatedSubstringPattern(s2))
}
