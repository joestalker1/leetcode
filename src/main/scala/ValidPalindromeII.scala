package leetcode

object ValidPalindromeII extends App {
  private def validPalindrome(s: String, from: Int, to: Int): Boolean = {
    var i = from
    var j = to
    while (i <= j) {
      if (s(i) != s(j)) return false
      i += 1
      j -= 1
    }
    true
  }

  def validPalindrome(s: String): Boolean = {
    var i = 0
    var j = s.length - 1
    var deleted = 0
    while (i <= j && deleted <= 1) {
      if (s(i) != s(j)) {
        if(validPalindrome(s, i + 1, j)) return true
        if(validPalindrome(s, i, j - 1)) return true
        deleted = Int.MaxValue
      } else {
        i += 1
        j -= 1
      }
    }
    deleted <= 1
  }

  println(validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
  println(validPalindrome("cbbbcg"))
  println(validPalindrome("eccer"))
  println(validPalindrome("cbbcc"))
  println(validPalindrome("aba"))
  println(validPalindrome("abca"))

}
