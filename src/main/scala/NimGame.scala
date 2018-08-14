trait NimGame {
  def canWinNim(n: Int): Boolean = {
    if (n == 0 || n == 1) false
    else n % 4 != 0
  }

}
