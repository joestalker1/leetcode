class MyQueue() {
  /** Initialize your data structure here. */
  private var front = List.empty[Int]
  private var back = List.empty[Int]

  private def check(): Unit = {
    if (front.isEmpty) {
      for (a <- back) {
        front = a :: front
      }
      back = List.empty[Int]
    }
  }

  /** Push element x to the back of queue. */
  def push(x: Int) {
    back = x :: back
  }

  /** Removes the element from in front of queue and returns that element. */
  def pop(): Int = {
    check()
    val top = front(0)
    front = front.tail
    top
  }

  /** Get the front element. */
  def peek(): Int = {
     check()
     front(0)
  }

  /** Returns whether the queue is empty. */
  def empty(): Boolean = front.isEmpty && back.isEmpty
}