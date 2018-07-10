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
        if (chars.get(ch).isEmpty) return false
        val freq = chars(ch) - 1
        if (freq == 0) chars = chars - ch
        else chars = chars + (ch -> freq)
      }
      chars.isEmpty
    }
  }

  println(isPerm("abc", "cbd"))
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
          i += 4
        } else i += 1
      }
    }
  }

  val s = "Mr John Smith    ".toCharArray
  urlify(s)
  println(s.mkString(""))
}

object Task1_4 {
  def isPermPolyn(s: String): Boolean = {
    if (s == null || s.isEmpty) false
    else {
      var freq = Map.empty[Char, Int]
      for (ch <- s) {
        freq = freq + (ch -> (freq.getOrElse(ch, 0) + 1))
      }
      if (s.length % 2 == 0) freq.filter { case (_, num) => num % 2 != 0 }.isEmpty
      else freq.filter { case (_, num) => num % 2 != 0 }.size == 1
    }
  }
}

object Task1_5 extends App {
  private def diffCount(s1: String, s2: String): Int = {
    if (s1 == null || s2 == null) 0
    else if (s1 == null) s2.length
    else if (s2 == null) s1.length
    else {
      var changes = 0
      val minLen = s1.length min s2.length
      var i = 0
      var j = 0
      while (i < minLen && j < minLen) {
        if (s1(i) != s2(j)) {
          changes += 1
          if (s1.length > s2.length) i += 1
          else if (s1.length < s2.length) j += 1
          else {
            i += 1
            j += 1
          }
        } else {
          i += 1
          j += 1
        }
      }
      if (i < s1.length - 1) changes += (s1.length - 1 - i)
      if (j < s2.length - 1) changes += (s2.length - 1 - j)
      changes
    }
  }

  def oneWay(s1: String, s2: String): Boolean = {
    //replace
    diffCount(s1, s2) <= 1
  }

  println(oneWay("kaler", "bales"))
}

object Task1_6 extends App {
  def compress(s: String): String = {
    if (s == null || s.isEmpty) s
    else {
      val sbf = new StringBuilder()
      var i = 0
      var c = 0
      while (i < s.length) {
        var j = i
        while (j < s.length && s(j) == s(i)) {
          j += 1
        }
        val c = j - i
        sbf.append(s(i))
        sbf.append(c)
        i = j
      }
      val newS = sbf.result()
      if (newS.length > s.length) s else newS
    }
  }

  println(compress("aabccccaaa"))
}

object Task1_7 extends App {
  def rotate(matrix: Array[Array[Short]]): Unit = {
    ()
  }
}

object Task1_8 extends App {
  private def fillRow(matrix: Array[Array[Int]], i:Int): Set[Int] = {
    var cols = Set.empty[Int]
    for(j <- 0 to matrix(0).length - 1){
      if(matrix(i)(j) == 0) cols = cols + j
      else matrix(i)(j) = 0
    }
    cols
  }
  def zero(matrix: Array[Array[Int]]): Unit = {
    var i = 0
    var cols = Set.empty[Int]
    while (i < matrix.length) {
      var j = 0
      cols = Set.empty[Int]
      while (j < matrix(0).length) {
        if (matrix(i)(j) == 0) {
          cols = cols ++ fillRow(matrix, i)
          j = Int.MaxValue
        }
        j += 1
      }
      i += 1
    }
    for {j <- cols} {
      for (i <- 0 to matrix.length - 1) matrix(i)(j) = 0
    }
  }
}

object Task1_9 extends App {
  def isSubstring(s1:String,s2:String):Boolean = {
    if(s1 == null || s2 == null || s1.isEmpty || s2.isEmpty) false
    else s1.indexOf(s2) != -1 || s2.indexOf(s1) != -1
  }

  def isRotation(s1:String,s2:String):Boolean = {
    if(s1 == null || s2 == null || s1.isEmpty || s2.isEmpty) false
    else{

    }
  }
}