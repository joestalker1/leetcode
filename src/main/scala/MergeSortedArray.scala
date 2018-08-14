package leetcode

/**
  * Created by jstalker on 16.07.17.
  */
trait MergeSortedArray {
  def merge(nums1: Array[Int], m: Int, nums2: Array[Int], n: Int): Unit = {
     var i = 0
     var j = 0
     var l = 0
     val end = nums1.length - 1
     while(i < m && j < n){
       if(nums1(m - 1 - i) > nums2(n - 1 - j)){
         nums1(end  - l) = nums1(m - 1 - i)
         i += 1
       } else {
         nums1(end - l) = nums2(n - 1 - j)
         j += 1
       }
       l += 1
     }
     if(j < n){
       while(j < n){
         nums1(end - l) = nums2(n - 1 - j)
         j += 1
         l += 1
       }
     }
     if(i < m){
      while(i < m){
        val a = nums1(m - 1 - i)
        nums1(end - l) = a
        i += 1
        l += 1
      }
    }
  }
}

object MergeSortedArrayApp extends MergeSortedArray with App {
  val a1 = Array(1, 5, 7, 0, 0, 0)
  val a2 = Array(2, 3, 5)
  merge(a1, 3, a2, 3)
  println(a1.mkString(","))
}