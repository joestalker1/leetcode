object NextGreaterElementI extends App {
  def nextGreaterElement(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
      if(nums1.isEmpty || nums2.isEmpty) Array.empty
      else {
        val res = Array.ofDim[Int](nums1.length)
        var stack = List.empty[Int]
        var map = Map.empty[Int, Int]
        for(a <- nums2){
          while(stack.nonEmpty && stack(0) < a){
             val top = stack(0)
             stack = stack.tail
             map = map + (top -> a)
          }
          stack = a :: stack
        }
        stack.foreach{a =>
          map = map + (a -> -1)
        }
        for(i <- 0 to nums1.length - 1) {
           val b = map(nums1(i))
           res(i) = b
        }
        res
      }
  }

  println(nextGreaterElement(Array(4,1,2), Array(1,3,4,2)).mkString(","))

}
