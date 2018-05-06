package leetcode

object ThirdMaximumNumber extends App {

  def thirdMax(nums: Array[Int]): Int = {
    var max1: Option[Int] = None
    var max2: Option[Int] = None
    var max3: Option[Int] = None
    for (n <- nums) {
      if(max1.exists(n == _) || max2.exists(n == _) || max3.exists(n == _)) {}
      else
      if (max1.isEmpty|| max1.exists(n > _)) {
          max3 = max2
          max2 = max1
          max1 = Some(n)
        } else if (max2.isEmpty || max2.exists(n > _)) {
          max3 = max2
          max2 = Some(n)
        } else if (max3.isEmpty || max3.exists(n > _)) max3 = Some(n)
      }
      max3.orElse(max1).get
  }

//  private def findMedian(arr: Array[Int],from: Int, n: Int):Int = {
//     val sorted = arr.slice(from, from + n).sorted
//     sorted(n / 2)
//  }
//
//  private def kthBiggest(arr: Array[Int], l:Int, r: Int,k: Int):Int = {
//     if(k > 0 && k <= (r - l + 1)) {
//        val n = r - l + 1
//
//        var i = 0
//        val median = Array.ofDim[Int]((n + 4)/ 5)
//        while(i < (n / 5)) {
//          median(i) = findMedian(arr,l + i * 5, 5)
//          i += 1
//        }
//        if(i * 5 < n){
//          median(i) = findMedian(arr, l + i * 5, n % 5)
//          i += 1
//        }
//        val medOfMed = if(i == 1) median(i-1) else kthBiggest(median, 0, i - 1, i / 2)
//        val pos = partition(arr, l, r, medOfMed)
//        if(pos - l == k - 1)  arr(pos)
//        else if(pos - l > (k - 1)) kthBiggest(arr, l, pos - 1, k)
//        else kthBiggest(arr, pos + 1, r, k - pos + l - 1)
//
//     } else arr.max
//
//  }
//
//  private def partition(arr: Array[Int], l: Int, r: Int, x: Int): Int = {
//      var i = l
//      var found = false
//      while(i < r && !found){
//          if(arr(i) == x) found = true
//          else i += 1
//      }
//      swap(arr, i, r)
//      i = l
//      var j = l
//      while(j <= (r - 1)){
//         if(arr(j) >= x){
//            swap(arr, i, j)
//            i+=1
//         }
//         j += 1
//
//      }
//      swap(arr, i, r)
//      i
//  }
//
//  private def swap(arr: Array[Int], i:Int, j: Int):Unit = {
//     val t = arr(i)
//     arr(i) = arr(j)
//     arr(j) = t
//  }


  val arr = Array(3, 2, 1)
  println(thirdMax(arr))
  val arr1 = Array(1, 1, 2)
  println(thirdMax(arr1))
  val arr2 = Array(2,2,3,1)
  println(thirdMax(arr2))
  val arr3 = Array(1,2,2,5,3,5)
  println(thirdMax(arr3))
  val arr4 = Array(1,2, Int.MinValue)
  println(thirdMax(arr4))
}
