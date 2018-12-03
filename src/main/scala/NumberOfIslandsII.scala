import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer

object NumberOfIslandsII extends App {
  case class Land(var parent: Int, var rank: Int = 0)

  private def find(sub: ArrayBuffer[Land], i: Int):Int = {
     if(sub(i).parent != i)  sub(i).parent = find(sub, sub(i).parent)
     sub(i).parent
  }

  private def union(sub: ArrayBuffer[Land], x:Int, y:Int): Unit = {
     val xroot = find(sub, x)
     val yroot = find(sub, y)
    if (sub(xroot).rank < sub(yroot).rank)
      sub(xroot).parent = yroot
    else if (sub(xroot).rank > sub(yroot).rank)
      sub(yroot).parent = xroot
    else {
       sub(yroot).parent = xroot
       sub(xroot).rank += 1
    }
  }

  private def add(map: mutable.HashMap[(Int, Int), Int], islands: ArrayBuffer[Land], r: Int,c: Int):Land = {
    val j = islands.size
    map += ((r,c) -> j)
    val land = Land(j)
    islands += land
    land
  }

  private def union(map: mutable.HashMap[(Int, Int), Int], islands: ArrayBuffer[Land], land: Land, r:Int, c:Int): Unit = {
    val i = map((r, c))
    union(islands, i, land.parent)
  }

  def numIslands2(m: Int, n: Int, positions: Array[Array[Int]]): List[Int] = {
      val map = mutable.HashMap[(Int, Int), Int]()
      val islands = new ArrayBuffer[Land]()

    (for(position <- positions) yield {
        //add land
        val r = position(0)
        val c = position(1)
        val island = add(map, islands, r, c)
        if(r + 1 < m && map.contains((r + 1, c)))
          union(map, islands, island, r + 1, c)
        if(r - 1 >= 0 && map.contains((r - 1, c)))
          union(map, islands, island, r - 1, c)
        if( c + 1 < n && map.contains((r, c + 1)))
          union(map, islands, island, r, c + 1)
        if(c - 1 >= 0 && map.contains((r, c - 1)))
          union(map, islands, island, r, c - 1)
        // count roots
        map.count{case (_, i) => islands(i).parent == i}
      }).toList
  }

  numIslands2(3, 3, Array( Array(0,1),Array(1,2),Array(2,1),Array(1,0),Array(0,2),Array(0,0),Array(1,1) ))
    //[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
}
