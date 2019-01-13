import scala.collection.mutable.Map

object WordBreak extends App {
  private def wordBreak(s:String, wordDict: List[String],pos: Int, mem: Map[(Int,Int), Boolean]):Boolean = {
     if(pos > s.length) false
     else
     if(pos == s.length) true
     else {
       var i = 0
       var comp = false
       while(i < wordDict.length && !comp){
         if(mem.contains((pos, i))) {
//            println(s"${pos} - ${i}")
            return mem((pos, i))
         }
         if(s.startsWith(wordDict(i), pos)) {
           comp = wordBreak(s, wordDict, pos + wordDict(i).length, mem)
           mem += ((pos + wordDict(i).length, i) -> comp)
         }
         i += 1
       }
       comp
     }
  }

  def wordBreak(s: String, wordDict: List[String]): Boolean = {
     if(s.isEmpty || wordDict.isEmpty) false
     else {
        val segs = Array.ofDim[Boolean](s.length + 1)
        segs(0) = true
        var j = 1
        while(j <= s.length) {
          var i = 0
          while(i < wordDict.length){
             if((j - wordDict(i).length) >= 0 && segs(j - wordDict(i).length)){
                segs(j) = segs(j) || segs(j - wordDict(i).length) && s.startsWith(wordDict(i), j - wordDict(i).length)
             }
             i += 1
          }
          j += 1
        }
        segs(s.length)
     }
  }

  println(wordBreak("ccaccc", List("cc","ac")))

  val s  = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
  val wordDict = List("a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa")
  println(wordBreak(s, wordDict))

  println(wordBreak("catsandog", List("cats", "dog", "sand", "and", "cat")))

   println(wordBreak("applepenapple",List("apple", "pen")))
}
