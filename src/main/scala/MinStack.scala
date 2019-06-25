class MinStack() {

  private var stack: List[Long] = Nil
  private var min: Long = 0l

  def push(x: Int) {
     if(stack.isEmpty){
       stack = x :: stack
       min = x
     } else if(x < min){
       val y = 2 * x - min
       stack = y :: stack
       min = x
     } else stack = x :: stack
  }

  def pop() {
     if(stack.nonEmpty){
       val x = stack.head
       if(x < min) {
         val newMin = 2* min - x
         min = newMin
       }
     }
  }

  def top(): Int = {
     stack.head.toInt
  }

  def getMin(): Int = {
     min.toInt
  }
}