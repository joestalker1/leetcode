package dynprog

object AddSum extends App {
  def add(arr: Array[Int], i: Int): Int = {
    if (i == 0) arr(0)
    else {
      arr(i) = arr(i) + add(arr, i - 1)
      arr(i)
    }
  }

  var arr = Array(1,2,3,4,5,6)
  add(arr, arr.length - 1)
  println(arr.mkString(" "))
}
