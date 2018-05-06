package leetcode

object LongestPalindromicSubstring extends App {
  def longestPalindrome(s: String): String = {
    var max1 = 0
    var maxs = ""
    for {i <- 0 to s.size - 2
    } {
      val s1 = longestPalindrome2(s, i, s.size - 1)
      if (s1.size > max1) {
          maxs = s1
        }
        max1 = max1 max s1.size
    }
    maxs
  }

  def longestPalindrome2(s: String, from: Int, to: Int): String = {
    if (to - from == 1) {
      val s1 = s.substring(from, to + 1)
      if (s1 == s1.reverse) s1
      else ""
    } else {
      var max1 = 0
      var maxs = ""
      for (sz <- 1 to (to - from + 1)) {
        val s1 = longestPalindrome2(s, from, from + sz)
        if (s.size > max1) {
          max1 = s.size
          maxs = s1
        }
      }
      maxs
    }
  }


  println(longestPalindrome(""))

  println(longestPalindrome("babad"))

  println(longestPalindrome("cbbd"))
}
