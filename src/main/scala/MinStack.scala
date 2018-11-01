import scala.collection.mutable

class MinStack() {

  /** initialize your data structure here. */
  private var stack: List[Int] = Nil
  private var minStack:List[Int] = Nil

  def push(x: Int) {
     stack = x :: stack
     if(minStack.isEmpty || minStack.head >= x) minStack = x :: minStack
  }

  def pop() {
     val x = stack.head
     stack = stack.tail
     if(minStack.head == x) minStack = minStack.tail
  }

  def top(): Int = {
     stack.head
  }

  def getMin(): Int = {
     minStack.head
  }
}