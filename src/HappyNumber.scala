package leetcode

object HappyNumber extends App {
  def isHappy(n: Int): Boolean = {
    isHappy(n, Map.empty[Int,Int])
  }

  private def isHappy(n:Int,seen:Map[Int,Int]):Boolean = {
    if(n == 1) true
    else if(seen.contains(n) && seen(n) > 1) false
    else {
      var na = n
      var digits = List.empty[Int]
      while (na != 0) {
        val r = na % 10
        digits = digits :+ r
        na /= 10
      }
      if (digits.isEmpty) false
      else {
        na = digits.map(a => a * a).sum
        val c = seen.getOrElse(n, 0)
        val nseen = seen + (n ->(c + 1))
        isHappy(na, nseen)
      }

    }

  }

  val a = 19
  println(isHappy(2))
}
