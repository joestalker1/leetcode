trait Amazon_ReverseWordsStringII {
  def reverseSubstring(str: Array[Char],from: Int,to: Int):Unit = {
    var i = from
    var j = to
    while(i < j){
      val ch = str(i)
      str(i) = str(j)
      str(j) = ch
      i += 1
      j -= 1
    }
  }

  def reverseWords(str: Array[Char]): Unit = {
    if (str == null) ()
    else {
      reverseSubstring(str,0, str.length - 1)
      var i = 0
      while(i < str.length){
          var j = i+1
          while(j < str.length && str(j) != ' ') j+=1
          j -= 1
          reverseSubstring(str, i, j)
          i = j + 2
      }
    }
  }
}

object Amazon_ReverseWordsStringIIApp extends Amazon_ReverseWordsStringII with App {
  val str = "".toCharArray
  reverseWords(str)
  println(str.mkString(""))
}
