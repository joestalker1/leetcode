class LongestPolindromicSubstring {
  def longestPalindrome(s: String): String = {
    if (s == null || s.isEmpty) ""
    else
    if (s.nonEmpty && s.count(_ == s(0)) == s.size) s // all letters are the same
    else {
      val poly = Array.ofDim[Int](s.size, s.size)
      var maxs = 1
      var a = (0, 0)
      for (l <- 2 to s.size) {
        for {i <- 0 to s.size - 1} {
          val j = i + l - 1
          if (j < s.size) {
            if (l == 2) {
              if (s(i) == s(j)) {
                poly(i)(j) = 2
                if (poly(i)(j) > maxs) {
                  maxs = poly(i)(j)
                  a = (i, j)
                }
              }
            } else {
              if (l % 2 == 0) {
                if (poly(i + 1)(j - 1) > 0) {
                  if (s(i) == s(j)) {
                    poly(i)(j) = poly(i + 1)(j - 1) + 2
                    if (poly(i)(j) > maxs) {
                      maxs = poly(i)(j)
                      a = (i, j)
                    }
                  }
                }
              } else {
                if (isPoly(s, i, j)) {
                  poly(i)(j) = l
                  if (poly(i)(j) > maxs) {
                    maxs = poly(i)(j)
                    a = (i, j)
                  }
                }
              }
            }
          }
        }
      }
      s.substring(a._1, a._2 + 1)
    }
  }

  @inline
  private def isPoly(s: String, i: Int, j: Int): Boolean = {
    var sz = j - i
    var i1 = i
    while (sz >= 0 && s(i + sz) == s(i1)) {
      sz -= 1
      i1 += 1
    }
    sz < 0
  }

}
