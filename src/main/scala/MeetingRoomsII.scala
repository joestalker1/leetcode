
object MeetingRoomsII extends App {
  class Interval(var _start: Int = 0, var _end: Int = 0) {
    var start: Int = _start
    var end: Int = _end
  }

  def minMeetingRooms(intervals: Array[Interval]): Int = {
    if (intervals == null || intervals.isEmpty) 0
    else {
      val sortedByStart = intervals.sortBy(_._start)
      val rooms = Array.fill[Int](sortedByStart.length)(-1)
      rooms(0) = sortedByStart(0)._end
      for (j <- 1 to sortedByStart.length - 1) {
        var l = 0
        while(l < rooms.length && rooms(l) != -1){
          if(sortedByStart(j)._start >= rooms(l)) {
            rooms(l)= sortedByStart(j)._end
            l = rooms.length
          } else l += 1
        }
        if(l < rooms.length && rooms(l) == -1) rooms(l) = sortedByStart(j)._end
      }
      rooms.count(_ != -1)
    }
  }

  implicit def apply(startEnd: (Int, Int)): Interval = new Interval(startEnd._1, startEnd._2)

  //println(minMeetingRooms(Array[Interval]( (0, 30),(5, 10),(15, 20))))
  //println(minMeetingRooms(Array[Interval]((7,10),(2,4))))
  println(minMeetingRooms(Array[Interval]((1293, 2986), (848, 3846), (4284, 5907), (4466, 4781), (518, 2918), (300, 5870))))
  println(minMeetingRooms(Array[Interval]((13, 15), (1, 13))))
  println(minMeetingRooms(Array[Interval]((1, 5), (8, 9), (8, 9))))
}


