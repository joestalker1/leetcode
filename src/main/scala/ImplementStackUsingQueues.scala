class MyStack() {
  /** Initialize your data structure here. */
  private var underlaying: List[Int] = Nil

  /** Push element x onto stack. */
  def push(x: Int) {
     underlaying = x :: underlaying
  }

  /** Removes the element on top of the stack and returns that element. */
  def pop(): Int = {
     if(underlaying.isEmpty) throw new RuntimeException("Stack is empty")
     val front = underlaying.head
     underlaying = underlaying.tail
     front
  }

  /** Get the top element. */
  def top(): Int = {
    if(underlaying.isEmpty) throw new RuntimeException("Stack is empty")
    underlaying.head
  }

  /** Returns whether the stack is empty. */
  def empty(): Boolean = {
     underlaying.isEmpty
  }
}
