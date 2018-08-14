package cracking_code_interview

// Task3_1 dont implement
object Task3_2 extends App {

  class MinStack {
    private var mina: Int = Int.MaxValue
    private var stack = List.empty[Int]

    def push(a: Int): Unit = {
      if (a < mina) {
        stack = (2 * a - mina) :: stack
        mina = a
      } else stack = a :: stack
    }

    def pop(): Int = {
      val x = stack.head
      stack = stack.tail
      if (x < mina) {
        mina = 2 * mina - x
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
      a = x :: a
    }

    def dequeue(): Int = {
      if (b.isEmpty && a.isEmpty) throw new NoSuchElementException
      if (b.isEmpty) {
        while (a.nonEmpty) {
          b = a.head :: b
          a = a.tail
        }
      }
      val x = b.head
      b = b.tail
      x
    }
  }

}

object Task3_5 extends App {

  class MyStack {
    private var a: List[Int] = Nil

    def push(x: Int): Unit = a = x :: a

    def isEmpty(): Boolean = a.isEmpty

    def peek(): Int = {
      if (a.isEmpty) throw new NoSuchElementException
      a.head
    }

    def pop(): Int = {
      if (a.isEmpty) throw new NoSuchElementException
      val x = a.head
      a = a.tail
      x
    }
  }

  class SortedStack {
    private val a = new MyStack()
    private val b = new MyStack()

    def push(x: Int): Unit = {
      if (a.isEmpty()) a.push(x)
      else {
        while (!a.isEmpty() && x > a.peek()) b.push(a.pop())
        a.push(x)
        while (!b.isEmpty()) a.push(b.pop())
      }
    }

    def pop(): Int = a.pop()

    def isEmpty(): Boolean = a.isEmpty()

    def peek(): Int = a.peek()
  }

  val sortedStack = new SortedStack()
  sortedStack.push(10)
  sortedStack.push(5)
  sortedStack.push(11)

  println(sortedStack.pop())
  println(sortedStack.pop())
  println(sortedStack.pop())
}

object Task3_6 extends App {
   sealed trait Animal {
     val arrivedAt: Long
  }
  case class Dog(arrivedAt: Long) extends Animal
  case class Cat(arrivedAt: Long) extends Animal
  private var cats = scala.collection.immutable.Queue[Cat]()
  private var dogs = scala.collection.immutable.Queue[Dog]()
  private var count: Long = 0

  def enqueue(animal:Animal):Unit = animal match {
    case Dog(_) => dogs = dogs.enqueue(Dog(count + 1))
                   count += 1
    case Cat(_) => cats = cats.enqueue(Cat(count + 1))
                   count += 1
  }

  def dequeueAny():Animal = {
    if(cats.isEmpty && dogs.isEmpty) throw new NoSuchElementException()
    if(dogs.head.arrivedAt < cats.head.arrivedAt) dequeueDog() else dequeueCat()
  }

  def dequeueCat(): Cat = {
    val (animal,newCats) = cats.dequeue
    cats = newCats
    animal
  }

  def dequeueDog(): Dog = {
    val (animal, newDogs) = dogs.dequeue
    dogs = newDogs
    animal
  }
}