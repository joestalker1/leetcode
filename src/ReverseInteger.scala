package leetcode

object ReverseInteger2 extends App {
  def reverse(x: Int): Int = {
     var rev = 0
     var b = x
     while(b != 0){
       val a = b & 0x1
       rev = rev << 1
       rev += a
       b = b >> 1
     }
     if(rev > 0 && x > 0 || rev < 0 && x < 0) rev else 0
  }

  println(reverse(123))
}
