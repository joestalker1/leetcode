package leetcode

object LongestPalindromicSubstring extends App {

  def longestPalindrome(str: String): String = {
    var maxLength = 1
    var start  = 0
    val len = str.length

    var low = 0
    var high = 0

    // One by one consider every character as center
    // point of even and length palindromes
    var i = 1
    while (i < len) { // Find the longest even length palindrome with
      // center points as i-1 and i.
      low = i - 1
      high = i
      while (low >= 0 && high < len && str(low)==str(high)) {
        if (high - low + 1 > maxLength) {
          start = low
          maxLength = high - low + 1
        }
        low -= 1
        high += 1
      }
      low = i - 1
      high = i + 1
      while (low >= 0 && high < len && str(low) == str(high)) {
        if (high - low + 1 > maxLength) {
          start = low
          maxLength = high - low + 1
        }
        low -= 1
        high += 1
      }
      i += 1
    }
    str.substring(start, start + maxLength)
  }

  //println(longestPalindrome(""))

  println(longestPalindrome("babad"))

  println(longestPalindrome("cbbd"))
}
