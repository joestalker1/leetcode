object Fibonachi extends App {
  private def fib(n:Int,a: Int,b: Int):Int = {
    if(n == 0) a
    else if(n == 1) b
    else fib(n-1,b, a + b)
  }
  def fib(n:Int):Int = fib(n,0, 1)
  println(fib(1000))
}

object ListApp extends App {
  private def reverse[T](list:List[T], acc:List[T]):List[T] = {
     if(list.isEmpty) acc
     else reverse(list.tail, list.head :: acc)
  }

  def reverse[T](list:List[T]):List[T] = reverse(list, Nil)

  println(reverse((1 to 1000).toList).mkString(","))
}