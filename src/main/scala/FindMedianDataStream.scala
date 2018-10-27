import scala.collection.mutable.PriorityQueue

class MedianFinder() {
  private val minOrd = Ordering.fromLessThan[Int](_ < _)
  private val maxHeap = new PriorityQueue[Int]()(minOrd)
  private val minHeap = new PriorityQueue[Int]()(minOrd.reverse)
  private var median: Double = 0

  private def updateMedian(e: Int): Unit = {
    if(maxHeap.size > minHeap.size){
       if(e < median){
          val maxA = maxHeap.dequeue()
          minHeap.enqueue(maxA)
          maxHeap.enqueue(e)
       } else minHeap.enqueue(e)
       median = (maxHeap.head + minHeap.head).toDouble / 2
    } else if(maxHeap.size == minHeap.size) {
      if(e < median){
         maxHeap.enqueue(e)
         median = maxHeap.head
      } else {
        minHeap.enqueue(e)
        median = minHeap.head
      }
    } else if(maxHeap.size < minHeap.size){
      if(e < median){
         maxHeap.enqueue(e)
      } else {
         val minA = minHeap.dequeue()
         maxHeap.enqueue(minA)
         minHeap.enqueue(e)
      }
      // Both heaps are balanced
      median = (minHeap.head + maxHeap.head).toDouble / 2
    }

  }

  def addNum(num: Int):Unit = {
     updateMedian(num)
  }

  def findMedian(): Double = median
}

object MedianFinderApp extends App {
   val medianFinder = new MedianFinder()
   medianFinder.addNum(6)
   println(medianFinder.findMedian())
   medianFinder.addNum(10)
   println(medianFinder.findMedian())
   medianFinder.addNum(2)
   println(medianFinder.findMedian())

//   medianFinder.addNum(4)
//   medianFinder.addNum(5)
   println(medianFinder.findMedian())
}
