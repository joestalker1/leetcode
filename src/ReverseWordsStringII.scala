object ReverseWordsStringII extends App {
  private def reverseWord(str: Array[Char], from: Int, to: Int): Unit = {
    var i = from
    var j = to
    while (i <= j) {
      val ch = str(i)
      str(i) = str(j)
      str(j) = ch
      i += 1
      j -= 1
    }
  }

  def reverseWords(str: Array[Char]): Unit = {
    if (str.isEmpty) ()
    else {
      var start = -1
      var end = -1
      var j = 0
      while (j < str.length) {
        val ch = str(j)
        if (start == end && end == -1) {
          start = j
          end = j
        } else if (j == str.length - 1 || ch == ' ') {
          reverseWord(str, start, end)
          start = -1
          end = -1
        } else end += 1
        j += 1
      }
    }
  }
  val words = "the sky is blue".toCharArray
  reverseWords(words)
  println(words.mkString(""))
}
