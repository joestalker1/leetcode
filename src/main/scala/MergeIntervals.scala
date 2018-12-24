

import scala.collection.mutable.ListBuffer

object MergeIntervals extends App {
  case class Interval(var _start: Int = 0, var _end: Int = 0) {
    var start: Int = _start
    var end: Int = _end
  }

  def merge(intervals: List[Interval]): List[Interval] = {
    if(intervals == null || intervals.length < 1) intervals
    else {
      var i = 0
      val sorted = intervals.sortBy(_._start)
      val res = new ListBuffer[Interval]()
      while(i < sorted.length){
        if(res.isEmpty || res.last._end < sorted(i)._start) res += intervals(i)
        else if(res.last._end >= sorted(i)._start)
            res(res.length-1) = res.last.copy(_end = (res.last._end max sorted(i)._end))
        i += 1
      }
      res.toList
    }
  }
  val intervals = List(Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18))
  println(merge(intervals))
}