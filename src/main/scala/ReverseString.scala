trait ReverseString {
  def reverseString(s: String): String = {
    if (s == null || s.isEmpty) s
    else {
      var stack = List.empty[Char]
      for (ch <- s) stack = ch :: stack
      val sbf = new StringBuilder
      for (ch <- stack) sbf.append(ch)
      sbf.result()
    }
  }
}

object ReverseStringApp extends ReverseString with App {
   println(reverseString("abc"))
}
