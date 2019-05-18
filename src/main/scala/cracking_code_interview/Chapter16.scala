package cracking_code_interview

//492,716,737
object Task16_1 extends App {
  def swap(a: Int, b: Int): (Int, Int) = {
    var b1 = b
    var a1 = a
    a1 = a1 + b1
    b1 = a1 - b1 // <- a1
    a1 = a1 - b1 // < - b1
    (a1, b1)
  }
}

//489,536
object Task16_2 extends App {
  def freq(book: List[String], word: String): Int = {
    0
  }
}

//465,472,497,517,527
object Task16_3 {
  def intersection(p1: (Int, Int), p2: (Int, Int), p3: (Int, Int), p4: (Int, Int)): (Int, Int) = {
    val k1 = (p1._2 - p2._2) / (p1._1 - p2._1)
    // y = k1x + b1
    val k2 = (p3._2 - p3._2) / (p3._1 - p4._1) // y = k2x + b2
    val b1 = p1._2 - k1 * p1._1
    val b2 = p3._2 - k2 * p3._1
    if ((k1 * p3._1 + b1) * (k1 * p4._1 + b1) < 0 && (k2 * p1._1 + b2) * (k2 * p2._1 + b2) < 0) {
      (0, 0)
    } else (Int.MaxValue, Int.MaxValue)
  }
}
//710,732
object Task16_4 extends App {
}
//585,711,729,733,745
object Task16_5 extends App {
  def trailingZero(n:Int): Int = {
     var count2 = 0
     var count5 = 0
     for(a <- 2 to n){
       if(a % 2 == 0) count2 += 1
       if(a % 5 == 0) count5 += 1
     }
     count2 min count5
  }
  println(trailingZero(10))
}
//632,670,679
//object Task16_6 extends App {
//   def smallDif(arr1:Array[Int],arr2:Array[Int]):(Int,Int) = {
//
//   }
//}