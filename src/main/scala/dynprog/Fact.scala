package dynprog

object Fact extends App {
   private def fact1(n:Int):Int = {
     if(n == 1) 1
     else n * fact1(n - 1)
   }

   def fact(n: Int): Int = fact1(n * n)

   def fact3(n: Int):Int = {
      if(n == 0) 1
      else{
        var i = 1
        var f = 1
        while(i <= n){
          f = f * i
          i += 1
        }
        f
      }
   }

   println(fact1(3))
}
