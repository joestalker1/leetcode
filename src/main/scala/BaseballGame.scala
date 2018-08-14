object BaseballGame extends App {
  def calPoints(ops: Array[String]): Int = {
      if(ops.isEmpty) 0
      else{
        var points = 0
        var scores = List.empty[Int]
        for(op <- ops){
          if(op == "D"){
            val last = scores.head * 2
            scores = last :: scores
            points += last
          } else if(op == "C"){
            val last = scores.head
            scores = scores.tail
            points -= last
          } else if(op == "+"){
             val a = scores(0)
             val b = scores(1)
             val c = a + b
             scores = c :: scores
             points += c
          } else {
             val a = op.toInt
             scores = a :: scores
             points += a
          }
        }
        points
      }
  }
  println(calPoints(Array("5","-2","4","C","D","9","+","+")))
  println(calPoints(Array("5","2","C","D","+")))
}
