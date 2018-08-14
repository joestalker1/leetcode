package leetcode

object JudgeRouteCircle extends App {
  def judgeCircle(moves: String): Boolean = {
     var p = (0, 0)
     for(dir <- moves){
        if(dir == 'U') p = p.copy(_2 = p._2 - 1)
        else if (dir == 'D') p = p.copy(_2 = p._2 + 1)
        else if(dir == 'R') p = p.copy(_1 = p._1 + 1)
        else if(dir == 'L') p = p.copy(_1 = p._1 - 1)
     }
     p == (0, 0)
  }

  println(judgeCircle("UR"))
}