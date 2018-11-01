import scala.collection.mutable.ListBuffer

object LongPressedName extends App {
  private def tokenize(s:String): IndexedSeq[String] = {
     val list = new ListBuffer[String]()
     var i = 0
     while(i < s.length){
        var j = i + 1
        val sbf = new StringBuilder()
        sbf.append(s(i))
        while(j < s.length && s(i) == s(j)){
          sbf.append(s(j))
          j += 1
        }
        list.append(sbf.result())
        i = j
     }
     list.toIndexedSeq
  }

  def isLongPressedName(name: String, typed: String): Boolean = {
    if (name == null || typed == null || name.length > typed.length) false
    else {
      val tokens1 = tokenize(name)
      val tokens2 = tokenize(typed)
      var i = 0
      var j = 0
      var eq = true
      while(i < tokens1.length && eq && j < tokens2.length) {
         if(tokens1(i)(0) == tokens2(j)(0) && tokens1(i).length <= tokens2(j).length){
           i += 1
           j += 1
         } else eq = false
      }
      eq && i == tokens1.length
    }
  }
  println(isLongPressedName("leelee", "lleeelee"))//true
  println(isLongPressedName("kikcxmvzi", "kiikcxxmmvvzz")) // false
  println(isLongPressedName("alex", "aaleex")) // true
  println(isLongPressedName("saeed", typed = "ssaaedd")) //false
}
