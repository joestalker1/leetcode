object ContainerWithMostWater extends App {
  def maxArea(height: Array[Int]): Int = {
      if(height == null || height.length < 2) 0
      else {
         var p = 0
         var q = height.length - 1
         var maxCapacity = Int.MinValue
         while(p < q) {
            val h = height(q) min height(p)
            maxCapacity = (h * (q - p)) max maxCapacity
            if(height(p) < height(q)) p += 1
            else q -=1
         }
         maxCapacity
      }
  }

  val h = Array(1,8,6,2,5,4,8,3,7)
  println(maxArea(h))
}
