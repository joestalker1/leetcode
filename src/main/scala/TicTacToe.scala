
class TicTacToe(_n: Int) {

  /** Initialize your data structure here. */
  private val firstRows = Array.ofDim[Int](_n)
  private val firstCols = Array.ofDim[Int](_n)
  private val secondRows = Array.ofDim[Int](_n)
  private val secondCols = Array.ofDim[Int](_n)

  private def update(row:Int,col:Int, player:Int): Unit = {
     if(player == 1) {
       firstRows(row) +=1
       firstCols(col) += 1
     } else {
       secondRows(row) += 1
       secondCols(col) += 1
     }
  }

  private def doesWin(rows:Array[Int],cols:Array[Int]): Boolean = {
    var diag = 0
    for(i <- 0 until _n){
      if(rows(i) >= _n) return true
      if(cols(i) >= _n) return true
      if(rows(i) == 1 && cols(i) == 1) diag += 1
    }
    if(diag == _n) return true
    diag = 0
    for(i <- 0 until _n){
      if(rows(_n - 1 - i) == 1 && cols(i) == 1) diag += 1
    }
    diag == _n
  }

  private def doesWin(player: Int):Boolean = {
      if(player == 1) doesWin(firstRows, firstCols) else doesWin(secondRows, secondCols)
  }

  /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
  @param col The column of the board.
  @param player The player, can be either 1 or 2.
  @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
  def move(row: Int, col: Int, player: Int): Int = {
      update(row, col, player)
      if(doesWin(player)) player else 0
  }
}

object TicTacToeApp extends App {
   val game = new TicTacToe(2)
   game.move(0, 0, 1)
   game.move(0, 1, 2)
   println(game.move(1, 1, 1))
}