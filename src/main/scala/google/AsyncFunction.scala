package google

import scala.concurrent.{Await, Future, Promise}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._

object AsyncFunction extends App {
   def f(a: Int, callback: Int => Int): Future[Int] = {
     Thread.sleep(120)
     Future(callback(a+1))
   }

   def p(n: Int, f:(Int,Int => Int) => Future[Int]): Either[Throwable, Int] = {
       if(n == 0) Left(new NoSuchElementException)
       else {
          val promise = Promise[Int]()
          val callback:Int => Int = a =>{
            promise.success(a)
            a
          }
         val fut = promise.future
         try {
           val res = Await.result(fut, 50 microsecond)
           Right(res)
         }
         catch {
           case ex: Throwable => p(n-1, f)
         }
       }
   }

  println(p(5, f))
}
