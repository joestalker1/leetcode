import scala.collection.immutable.Queue

class MovingAverage(_size: Int) {
  private var window = Queue[Int]()
  private var prevSum = 0.0

  def next(a: Int): Double = {
    if(window.length == _size) {
      val (b, newWindow) = window.dequeue
      prevSum -= b
      window = newWindow
    }
    prevSum += a
    window = window.enqueue(a)
    prevSum / window.length
  }

}