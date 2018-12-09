import scala.collection.mutable.Map

object FruitIntoBaskets extends App {
  private def addFruit(basket: Map[Int,Int], a: Int):Unit = {
     val fruits = basket.getOrElse(a, 0)
     basket += (a -> (fruits + 1))
  }

  private def removeFruit(basket: Map[Int,Int], b:Int):Unit = {
     val fruits = basket.getOrElse(b, 0)
     if(fruits - 1 <= 0) basket -= b
     else basket += (b -> (fruits - 1))
  }

  def totalFruit(tree: Array[Int]): Int = {
      if(tree == null) 0
      else if(tree.length < 3) tree.length
      else {
         var p = 0
         var q = p + 1
         val basket = Map.empty[Int, Int]
         var maxCollected = 0
         addFruit(basket, tree(p))
         //addFruit(basket, tree(q))
         while(p <= q && q < tree.length) {
           addFruit(basket, tree(q))
           if(basket.size <= 2) {
               maxCollected = maxCollected max (q - p + 1)
               q += 1
           } else {
             while(p <= q && basket.size > 2){
               removeFruit(basket, tree(p))
               p += 1
             }
             removeFruit(basket, tree(q))
           }
         }
         maxCollected
      }
  }

  val trees1 = Array(1,2,3,2,2) //4
  println(totalFruit(trees1))
  val trees2 = Array(3,3,3,1,2,1,1,2,3,3,4) //5
  println(totalFruit(trees2))
}
