object FirstUniqueCharacterString extends App {
  def firstUniqChar(s: String): Int = {
    if (s.isEmpty) -1
    else {
      val freq = Array.ofDim[Int](26)
      for(ch <- s) freq(ch - 'a') += 1
      for(i <- 0 until s.length){
        if(freq(s(i) - 'a') == 1) return i
      }
      -1
    }
  }

  val s = "loveleetcode"
  println(firstUniqChar(s))
}


