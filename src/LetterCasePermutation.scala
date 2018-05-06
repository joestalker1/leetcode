package leetcode

object LetterCasePermutation extends App {
  def letterCasePermutation(s: String): List[String] = {
       if(s.isEmpty) List.empty
       else {
          def letterPermutation(p:String, lastChar: Int,perms: List[String]):List[String] = {
             if(lastChar == p.length - 1) perms
             else {
               var newPerms = perms
               for(i <- lastChar + 1 until p.length-1) {
                 val ch = p(i)
                 if(ch.isLetter) {
                   val newString = p.substring(0, lastChar + 1) + (if(ch.isLower) ch.toUpper else ch.toLower) + p.substring(lastChar + 2)
                   newPerms = newString :: newPerms
                   newPerms = letterPermutation(newString, lastChar+1, newPerms)
                 } else newPerms = letterPermutation(p, lastChar + 1, newPerms)
               }
               newPerms
             }
          }
          letterPermutation(s, -1, s :: Nil)
       }
  }

  println(letterCasePermutation("a1b2").mkString(","))
}
