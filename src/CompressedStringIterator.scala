class StringIterator(_compressedString: String) {
  private var ptr = 0
  private var curChar: Char = ' '
  private var curCount = 0

  def next(): Char = {
    if (!hasNext()) ' '
    else {
      if (curCount == 0) {
        curChar = _compressedString(ptr)
        ptr += 1
        curCount = 0
        while(ptr < _compressedString.length && Character.isDigit(_compressedString(ptr))){
           curCount = 10 * curCount + _compressedString(ptr) - '0'
           ptr += 1
        }
      }
      curCount -= 1
      curChar
    }
  }

  def hasNext(): Boolean = _compressedString != null && _compressedString.nonEmpty && ptr < _compressedString.length || curCount > 0
}

object StringIteratorApp extends App {
  val si = new StringIterator("V1a2")
  (1 to 100).foreach{i =>
    println(si.next())
  }
  si.hasNext()

}