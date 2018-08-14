package leetcode

case class Seg(x: Int, y: Int) {
  override def equals(o: scala.Any): Boolean = o match {
    case seg: Seg => seg.x == x && seg.y == y
    case _ => false
  }

  override def hashCode(): Int = {
    val prime = 31
    prime * x + y
  }

  def dist(o: Seg): Int =
    scala.math.sqrt((x - o.x) * (x - o.x) + (y - o.y) * (y - o.y)).toInt

}

object NumberBoomerangs extends App {
  def numberOfBoomerangs(points: Array[Array[Int]]): Int = {
    if (points.isEmpty) 0
    else {
      val dist1 = scala.collection.mutable.Map[(Seg, Seg), Double]()
      val seen = scala.collection.mutable.Set[(Seg, Seg, Seg)]()
      for {i <- 0 until points.length
           j <- 0 until points.length if i != j
           k <- 0 until points.length if k != j && k != i
      } {
        val seg1 = Seg(points(i)(0), points(i)(1))
        val seg2 = Seg(points(j)(0), points(j)(1))
        val seg3 = Seg(points(k)(0), points(k)(1))
        val ifd1 = dist1.get(seg1 -> seg2)
        val d1 = if (ifd1.isEmpty) {
          val d = seg1.dist(seg2)
          dist1 += ((seg1 -> seg2) -> d)
          dist1 += ((seg2 -> seg1) -> d)
          d
        } else ifd1.get

        val ifd2 = dist1.get(seg1 -> seg3)
        val d2 = if (ifd2.isEmpty) {
          val d = seg1.dist(seg3)
          dist1 += ((seg1 -> seg3) -> d)
          dist1 += ((seg3 -> seg1) -> d)
          d
        } else ifd2.get
        if (d1 == d2) {
          if (!seen.exists(s => s._1 == seg1 && s._2 == seg2 && s._3 == seg3)) seen += Tuple3(seg1, seg2, seg3)
        }
      }
      seen.size
    }
  }

  val points = Array(Array(0, 0), Array(1, 0), Array(2, 0))
  println(numberOfBoomerangs(points))
}
