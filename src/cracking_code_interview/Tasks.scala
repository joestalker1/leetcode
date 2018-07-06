package cracking_code_interview

object Task1_1 extends App {
  def isUnique(s: String): Boolean = {
    if (s == null || s.isEmpty) false
    else {
      val met = Array.ofDim[Boolean](27)
      var unique = true
      for (ch <- s) {
        val index = ch - 'a'
        if (met(index)) unique = false
        else met(index) = true
      }
      unique
    }
  }
  println(isUnique("abcde"))
}


object Task1_2 extends App {
  def isPerm(s1: String, s2: String): Boolean = {
    if (s1 == null || s1.isEmpty || s2 == null || s2.isEmpty || s1.length != s2.length) false
    else {
      var chars = Map.empty[Char, Int]
      for (ch <- s1) {
        val freq = chars.getOrElse(ch, 0)
        chars = chars + (ch -> (freq + 1))
      }
      for (ch <- s2) {
        if(chars.get(ch).isEmpty) return false
        val freq = chars(ch) - 1
        if (freq == 0) chars = chars - ch
        else chars = chars + (ch -> freq)
      }
      chars.isEmpty
    }
  }
  println(isPerm("abc","cbd"))
}

object Task1_3 extends App {
  private def escapeSpace(s: Array[Char], i: Int): Unit = {
    var j = s.length - 1
    while (j >= i) {
      s(j) = s(j - 2)
      j -= 1
    }
    s(i) = '%'
    s(i + 1) = '2'
    s(i + 2) = '0'
  }

  def urlify(s: Array[Char]): Unit = {
    if (s == null || s.isEmpty) ()
    else {
      var i = 0
      while (i < s.length) {
        if (s(i) == ' ') {
          escapeSpace(s, i)
          i+=4
        } else  i += 1
      }
    }
  }

  val s = "Mr John Smith    ".toCharArray
  urlify(s)
  println(s.mkString(""))
}
