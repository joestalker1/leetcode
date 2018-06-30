class TwoSumIII() {
  private var numToFreq = Map.empty[Int, Int]

  def add(number: Int): Unit = {
    numToFreq = numToFreq + (number -> (numToFreq.get(number).map(_=> 2).getOrElse(1)))
  }

  /** Find if there exists any pair of numbers which sum is equal to the value. */
  def find(value: Int): Boolean = {
    var exist = false
    for (kv <- numToFreq if !exist) {
      val (num, freq) = kv
      val rem = value - num
      val remFreq = numToFreq.getOrElse(rem, 0)
      exist = (rem == num && freq > 1) || (rem != num && remFreq > 0)
    }
    exist
  }
}

object TwoSumAppIII extends App {
  val twoSum = new TwoSumIII()
  twoSum.add(3)
  twoSum.add(2)
  twoSum.add(1)
  List(2, 3, 4, 5, 6).foreach(a => println(twoSum.find(a)))
}