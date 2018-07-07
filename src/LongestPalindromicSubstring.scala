package leetcode

object LongestPalindromicSubstring extends App {
  private def reverseStr(s:String):String = {
    val sbf = new StringBuilder()
    for(i <- s.length - 1 to 0 by -1){
      sbf.append(s(i))
    }
    sbf.result()
  }

  private def extractPalyn(s: String, lcp: Array[Array[Int]], maxi :Int, maxj : Int): String = {
    var i = maxi
    var j = maxj
    val sbf = new StringBuilder()
    while(i >= 0 && j >= 0 && lcp(i)(j) != 0){
      if(lcp(i)(j) != 0) {
        sbf.append(s(i-1))
        i -= 1
        j -= 1
      } else i = -1
    }
    sbf.result()
  }

  def longestPalindrome(s: String): String = {
    if(s == null || s.isEmpty) s
    else {
      val rev = reverseStr(s)
      val lcp = Array.fill(s.length + 1, s.length + 1)(0)
      var maxLen = 0
      var maxi = -1
      var maxj = -1
      for{i <- 0 to s.length
          j <- 0 to rev.length
      } {
        if(i == 0 || j == 0) lcp(i)(j) = 0
        else if(s(i-1) == rev(j-1)) {
          lcp(i)(j) = lcp(i-1)(j-1) + 1
          if(maxLen < lcp(i)(j)){
            maxLen = lcp(i)(j)
            maxi = i
            maxj = j
          }
        }
      }
      extractPalyn(s, lcp, maxi, maxj)
    }
  }

  //println(longestPalindrome(""))

  println(longestPalindrome("babad"))

  println(longestPalindrome("cbbd"))
}
