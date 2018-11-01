package cracking_code_interview

object Task8_1 extends App {
   def tripleStep(n: Int): Int = {
     val ways = Array.ofDim[Int](n + 1)
     ways(1) = 1
     ways(2) = 2
     for(i <- 3 to n){
       ways(i) = 1 + ways(i - 1) + ways(i - 2)+ ways(i - 3)
     }
     ways(n)
    }
    println(tripleStep(7))
}

object Task8_2 extends App {

}