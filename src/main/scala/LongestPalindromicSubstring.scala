package leetcode

object LongestPalindromicSubstring extends App {
  def longestPalindrome(str: String): String = {
    if(str == null || str.isEmpty) null
    else {
      val dp = Array.fill(str.length)(Array.ofDim[Int](str.length))
      var i1 = 0
      var i2 = 0
      var maxLen = 0
      for(i <- 0 to str.length-1) dp(i)(i) = 1
      for{len <- 2 to str.length
          i <- 0 to str.length - len}{
        val j = i + len - 1
        if(str(i) == str(j) && len == 2) {
          dp(i)(j) = 2
          if(maxLen < dp(i)(j)) {
            maxLen = dp(i)(j)
            i1 = i
            i2 = j
          }
        }
        else
        if(str(i) == str(j)) {
          dp(i)(j) = 2 + dp(i+1)(j-1)
          if(maxLen < dp(i)(j)) {
            maxLen = dp(i)(j)
            i1 = i
            i2 = j
          }
        }
        else {
          val r1 = dp(i+1)(j)
          val r2 = dp(i)(j-1)
          if(maxLen < r1) {
            maxLen = dp(i+1)(j)
            i1 = i+1
            i2 = j
          } else if(maxLen < r2) {
            maxLen = dp(i)(j-1)
            i1 = i
            i2 = j-1
          }
          dp(i)(j) = r1 max r2
        }
      }
      str.substring(i1, i2+1)
    }
  }

  //println(longestPalindrome(""))

  println(longestPalindrome("acad"))

  println(longestPalindrome("cbbd"))
}
