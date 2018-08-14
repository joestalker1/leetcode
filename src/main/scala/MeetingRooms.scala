case class Interval(_start: Int, _end: Int)

object MeetingRooms extends App {
  private def sortByEnd(arr: Array[Interval], low: Int = 0, high: Int = arr.length - 1): Unit = {
    if (low < high) {
      val pi = partition(arr, low, high)
      sortByEnd(arr, low, pi - 1)
      sortByEnd(arr, pi + 1, high)
    }
  }

  private def partition(arr: Array[Interval], low: Int, high: Int): Int = {
    val pivot = arr(high)
    var j = low - 1
    for (i <- low until high) {
      if (arr(i)._end <= pivot._end) {
        j += 1
        val t = arr(j)
        arr(j) = arr(i)
        arr(i) = t
      }
    }
    val t = arr(j + 1)
    arr(j + 1) = pivot
    arr(high) = t
    j + 1
  }

  def canAttendMeetings(intervals: Array[Interval]): Boolean = {
     if(intervals.isEmpty) false
     else {
       sortByEnd(intervals)
       var j = 1
       while (j < intervals.length) {
         if(intervals(j-1)._end > intervals(j)._start || intervals(j-1)._start > intervals(j)._end) return false
         j += 1
       }
       true
     }
  }
  val arr = Array(Interval(0, 30), Interval(5, 10), Interval(15, 20))
  println(canAttendMeetings(arr))
}
