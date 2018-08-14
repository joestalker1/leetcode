
object Tree {
  sealed trait Tree[+T]

  case class Node[T](left: Tree[T], value: T, right: Tree[T]) extends Tree[T]

  case object Leaf extends Tree[Nothing]

  def member[T](root: Tree[T], x: T, lessOrEq: T)(implicit ord: Ordering[T]): Boolean = root match {
    case Leaf => lessOrEq == x
    case Node(left, value, right) => if(ord.lteq(x, value)) member(left, x, value)
    else member(right, x, lessOrEq)
  }
  def insert[T : Ordering](root: Tree[T], x: T):Tree[T] = root match {
    case Leaf => Node(Leaf, x, Leaf)
    case Node(left,value, right) => val ord = implicitly[Ordering[T]]
      if(ord.lt(x, value)) Node(insert(left, x), value, right)
      else if(ord.gt(x, value)) Node(left, value, insert(right, x))
      else root
  }
}
object OkasakiExcersise {
  def suffixes(list: List[Int]): List[List[Int]] = list match {
    case Nil => List.empty
    case _ :: xs => list :: suffixes(xs)
  }



}

object RunExcercise extends App {
  val list = List(1, 2, 3, 4)
  val res = OkasakiExcersise.suffixes(list)
}