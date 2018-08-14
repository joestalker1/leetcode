package leetcode

object IntersectionTwoArrays extends App {
  def intersection(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    if (nums1.isEmpty) Array.empty
    else if (nums2.isEmpty) Array.empty
    else {
      var map = Map.empty[Int, Int]
      map = map ++ nums1.map { i => (i -> 0)}
      map = map ++ nums2.filter(i => map.contains(i)).map(i => i -> i)
      map.filter { case (k, v) => v == k}.map(_._1).toArray
    }
  }
  val arr1 = Array(1, 2, 2, 1)
  val arr2 = Array(2, 2)
  println(intersection(arr1, arr2).mkString(","))
}
