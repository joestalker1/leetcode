package cracking_code_interview

// Task3_1 dont implement
object Task3_2 extends App {
  class MinStack {
    private var mina: Int = Int.MaxValue
    private var stack = List.empty[Int]
    def push(a:Int):Unit = {
      if(a < mina){
        stack = (2*a - mina) :: stack
        mina = a
      } else stack = a :: stack
    }

    def pop():Int = {
       val x = stack.head
       stack = stack.tail
       if(x < mina) {
         mina = 2*mina - x
         mina
       } else x
    }

    def min(): Int = mina
  }
}

object Task3_4 extends App {
   class Queue {
     private var a = List.empty[Int]
     private var b = List.empty[Int]

     def enqueue(x: Int): Unit = {
        if(a.isEmpty) a = x :: a

     }
   }
}