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
  def flipToWin(a:Integer):Int = {

  }
}