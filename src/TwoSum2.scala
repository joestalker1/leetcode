package leetcode

object TwoSum2 extends App {
  def twoSum(numbers: Array[Int], target: Int): Array[Int] = {
    var map = Map.empty[Int,Int]
    var i = 0
    var res = (0, 0)
    while(i < numbers.length) {
      map.get(numbers(i)).map { j =>
        res = (j, i)
        i = numbers.length
      }.getOrElse{
        map = map + ((target - numbers(i)) -> i)
      }
      i += 1
    }
    Array(res._1, res._2)
  }

  println(twoSum(Array(2, 7, 11, 15), 9).mkString(","))

}
