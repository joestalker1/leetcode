package leetcode

object ThePowerSum extends App {
  def powerSum(x: Int, n: Int): Int = {
    tryPowerSum(x, n, collection.mutable.Set.empty[Int])
  }

  private def tryPowerSum(x: Int, n: Int, seen: collection.mutable.Set[Int]): Int = {
    var count = 0
    var a = 1
    var p = powerOf(a, n)
    while (p <= x) {
      if (!seen(a)) {
        if (p == x && seen.nonEmpty) {
          count += 1
          seen += a
          println(seen.map(a => s"$a^2").mkString("+"))
          p += 1
        }
        else {
          seen += a
          val c1 = tryPowerSum(x - p, n, seen)
          count += c1
        }

      }
      a += 1
      p = powerOf(a, n)
    }
    count
  }


  @inline
  private def powerOf(a: Int, n: Int): Int = {
    var x1 = 1
    for (_ <- 1 to n) x1 *= a
    x1
  }


  println(powerSum(10, 2))
  println(powerSum(100, 2))

  //  def main(args: Array[String]) {
  //    val sc = new java.util.Scanner (System.in);
  //    var X = sc.nextInt();
  //    var N = sc.nextInt();
  //    val result = powerSum(X, N);
  //    println(result)
  //  }
}
