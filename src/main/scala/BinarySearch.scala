object BinarySearch extends App {
   def search(arr:Array[Int],x: Int):Option[Int] = {
      var k = 0
      var b = arr.length / 2
      while(b >= 1) {
        while(k + b < arr.length && arr(k + b) <= x) k += b
        b /= 2
      }
      if(arr(k) == x) Option(x) else None
   }

   val arr = Array(1, 3, 5, 10, 17, 21, 34, 45, 67, 70, 89, 90, 96)
   println(search(arr, 0))

}
