object LetterCasePermutation extends App {
  def letterCasePermutation(s: String): List[String] = {
    if (s.isEmpty) List("")
    else {
      def letterPermutation(p: String, curChar: Int, perms: Set[String]): Set[String] = {
         if(curChar >= p.length) perms
         else {
           var newPerms = Set.empty[String]
           for (i <- curChar until p.length) {
             val ch = p(i)
             var newString = p
             if (ch.isLetter) newString = p.substring(0, i) + (if (ch.isLower) ch.toUpper else ch.toLower) + p.substring(i + 1)
             newPerms = newPerms ++ letterPermutation(newString, i + 1, perms + newString)
           }
           newPerms
         }
      }

      letterPermutation(s, 0, Set(s)).toList
    }
  }
  println(letterCasePermutation("po"))
  println(letterCasePermutation("a1b2").mkString(","))
  println(letterCasePermutation("3z4").mkString(","))
}
