class Snake(spots:List[Spot]) {
   def eat(food: Food): Snake
   def canOverlap():Boolean

   def move(row:Int,col:Int):Snake {
      val spotDiff = Set(abs(spots(0).row - row) ,abs(spots(0).col - col))
       if(spotDiff == Set(0,1)) {
          val newSpots = List(Spot(row,col)) ++ spots.take(spots.length - 1)
          Snake(newSpots)
       } else {
          this
       }
   }
}

case class Food(row: Int, col: Int)

sealed trait GameStatus
object Win extends GameStatus
object Lost extends GameStatus


case class Board(snake: Snake, food:Map[(Int, Int),Food]) {
   def makeMove():Board {
       //check up,left,right,down
       val newSnake = snake.move()
       if(newSnake.canOverlap)
   }
}


case class Spot(row: Int,col: Int)


