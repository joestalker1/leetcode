import scala.collection.mutable.ListBuffer

case class WordNode(word: String, numSteps: Int, pre: WordNode = null)

object FindLaddersApp extends App {
  private def log(last: WordNode): Unit = {
     val sbf = new StringBuilder()
     var cur = last
     while(cur != null){
       sbf.insert(0, s"${cur.word}(${cur.numSteps})")
       cur = cur.pre
     }
     println(sbf.result())
  }

  def findLadders(beginWord: String, endWord: String, wordList: List[String]): List[List[String]] = {
      var result = List.empty[List[String]]
      var queue = List.empty[WordNode]
      queue = WordNode(beginWord,1) :: queue
      var minStep = 0
      var visited = Set.empty[String]
      var unvisited = Set.empty[String]
      unvisited = unvisited ++ wordList
      var preNumSteps = 0
      while(queue.nonEmpty){
          var top = queue.head
          queue = queue.tail
          val word = top.word
          val currNumSteps = top.numSteps
          log(top)
          println(s"currNumStep = $currNumSteps")
          var continue = false
          if(word == endWord){
               if(minStep == 0) minStep = top.numSteps
               if(top.numSteps == minStep && minStep !=0) {
                  //nothing
                  val t = new ListBuffer[String]()
                  t += top.word
                  while(top.pre !=null){
                      t.+=:(top.pre.word)
                      top = top.pre
                  }
                  result = result :+ t.toList
                  continue = true
              }
          }
          if(!continue){
              if(preNumSteps < currNumSteps){
                  unvisited = unvisited -- visited
              }
              println(s"preNumSteps = $preNumSteps")
              preNumSteps = currNumSteps
              val arr = word.toArray

              for(i <- 0 until arr.length) {
                  for(c <- 'a' to 'z'){
                      val temp = arr(i)
                      if(arr(i) != c){
                          arr(i) = c
                      }

                      val newWord = String.valueOf(arr)
                      if(unvisited.contains(newWord)) {
                          queue = queue :+ WordNode(newWord, top.numSteps + 1, top)
                          visited = visited + newWord
                      }
                      arr(i)=temp
                  }
              }

          }
      }
      result
  }
  println(findLadders("hit", "cog", List("hot","dot","dog","lot","log","cog")))
}