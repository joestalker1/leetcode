package cracking_code_interview

//137, 169, 215
object Task5_1 extends App{
  def insert(n: Int, m: Int,i:Int, j:Int):Int = {
      require(i < j)
      val rightMask = (1 << i) - 1
      var leftMask = (1 << (j+1)) - 1 //0001111
      leftMask = ~leftMask //111000
      val mask = leftMask | rightMask
      val a = m << i
      val c = (n & mask) | a
      c
  }
  insert(1 << 11, 0x13, 2, 6)
}
//143, 167,173, 269, 297
object Task5_2 extends App {
   def binToString(a: Double):String = {
      if (a > 1 || a < 0) ""
      else {
        var len = 0
        val buf = new StringBuilder()
        while(len <= 32) {
           val b = a * 2
           val integral = b.toInt
           buf.append(integral.toString)
           len += 1
        }
        buf.result()
      }
   }
}

//159, 226, 314, 352
object Task5_3 extends App {
  def flipToWin(a: Int):Int = {
      var c = a
      var curLen1 = 0
      var curLen2 = 0
      var zeros = 0
      var maxLen = 0
      while(c > 0) {
        maxLen = maxLen max (curLen1 + curLen2)
        val b = c << 1
        if(b == 1) {
          if(zeros == 1) {
            //we can flip it
            curLen2 = curLen1 + 1
            curLen1 = 0
          } else if(zeros > 0) {
            curLen1 = 0
            curLen2 = 0
          }
          curLen1 += 1
          zeros = 0
        } else zeros += 1
        c = c << 1
      }
      maxLen
  }
}
//147, 175,242, 312, 339, 358, 375, 390
object Task5_4 extends App {
   def nextNumber(a:Int):Int = {
    ???
   }
}
//151, 202,261,302,346,372,383,398
object Task5_5 extends App {
   // n & (n-1) if n is power of 2
}
/// 336, 369
object Task5_6 extends App {
   def convert(a:Int, b: Int):Int = {
     var xor = a ^ b
     var count = 0
     while(xor > 0) {
       val one = xor >> 1
       if(one > 0) count += 1
       xor = xor >> 1
     }
     count
   }
}
///145, 248, 328, 355
object Task5_7 extends App {
   def pairwiseSwap(a:Int):Int = ???
}

