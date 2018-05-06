package leetcode

object OneTwoBitsCharacters extends App {
  def isOneBitCharacter(bits: Array[Int]): Boolean = {
    if(bits.last == 0) isOneBitCharacter(bits.view(0, bits.length - 1), 0)
    else false
  }

  private def isOneBitCharacter(bits: IndexedSeq[Int],from: Int): Boolean = {
    if(from >= bits.length) true
    else
    if(bits.isEmpty) false
    else {
      //try 10
      val res1 = if(from < bits.length && (from + 1)  < bits.length && bits(from) == 1 && bits(from + 1) == 0) isOneBitCharacter(bits, from + 2) else false
      val res2 = if(!res1 && from < bits.length && (from + 1)  < bits.length && bits(from) == 1 && bits(from + 1) == 1) isOneBitCharacter(bits, from + 2) else false
      val res3 = if(!res2 && from < bits.length && bits(from) == 0) isOneBitCharacter(bits, from + 1) else false
      res1 || res2 || res3
    }
  }



  val arr1 = Array(1, 1, 1, 0)
  println(isOneBitCharacter(arr1))

  val arr2 = Array(0, 0, 0)
  println(isOneBitCharacter(arr2))

  val arr3 = Array(1, 0, 0)
  println(isOneBitCharacter(arr3))
}
