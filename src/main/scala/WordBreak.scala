object WordBreak extends App {
  private def findSub(s:String,sub:String, pos:Int):Boolean = {
    var i = pos
    var j = 0
    while(i < s.length && j < sub.length && s(i) == sub(j)){
      j += 1
      i += 1
    }
    j == sub.length
  }

  private def wordBreak(s:String, wordDict: List[String],pos: Int):Boolean = {
     if(pos > s.length) false
     else
     if(pos == s.length) true
     else {
       var i = 0
       var comp = false
       while(i < wordDict.length && !comp){
         if(findSub(s, wordDict(i), pos)){
           comp = wordBreak(s, wordDict,pos + wordDict(i).length)
         }
         i += 1
       }
       comp
     }
  }

  def wordBreak(s: String, wordDict: List[String]): Boolean = {
     if(s.isEmpty || wordDict.isEmpty) false
     else wordBreak(s, wordDict, 0)
  }

  println(wordBreak("catsandog", List("cats", "dog", "sand", "and", "cat")))

  println(wordBreak("applepenapple",List("apple", "pen")))
}
