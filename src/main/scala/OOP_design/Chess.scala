trait Color
object Black extends Color
object White extends Color

trait Piece {
  def color : Color
  def isKilled():Boolean
  def kill():Unit
  def canMove(board: Board,start:Spot,end:Spot):Boolean
}

case class Board(boxes:Array[Array[Spot]]) {

  reset()

  def getSpot(row:Int,col:Int):Option[Spot] = {
      if(row > 7 || row < 0 || col < 0 || col > 7)
         None
      else Option(boxes(row)(col))
  }

  def reset():Unit = {
        boxes[0][0] = new Spot(0, 0, Rook(White));
        boxes[0][1] = new Spot(0, 1, KnightWhite);
        boxes[0][2] = new Spot(0, 2, Bishop(White));
        //...
        boxes[1][0] = new Spot(1, 0, Pawn(White));
        boxes[1][1] = new Spot(1, 1, Pawn(White));
        //...

        // initialize black pieces
        boxes[7][0] = new Spot(7, 0, Rook(Black));
        boxes[7][1] = new Spot(7, 1, Knight(Black));
        boxes[7][2] = new Spot(7, 2, Bishop(Black));
        //...
        boxes[6][0] = new Spot(6, 0, Pawn(Black));
        boxes[6][1] = new Spot(6, 1, Pawn(Black));
        //...

        // initialize remaining boxes without any piece
        for (int i = 2; i < 6; i++) {
            for (int j = 0; j < 8; j++) {
                boxes[i][j] = new Spot(i, j);
            }
        }
  }
}

case class Bishop(color:Color) extends Piece {

}

case class Rook(color: Color) extends Piece {

}

case class King(color:Color) extends Piece {
    private var castlingDone: Boolean = false;

    def isCastlingDone():Boolean = {
        return this.castlingDone;
    }

    def void setCastlingDone(boolean castlingDone):Unit =  {
        this.castlingDone = castlingDone;
    }

    @Override
    override def canMove(Board board, Spot start, Spot end):Boolean = {
        // we can't move the piece to a Spot that
        // has a piece of the same color
        if (end.getPiece().isWhite() == this.isWhite()) {
            return false;
        }

        int x = Math.abs(start.getX() - end.getX());
        int y = Math.abs(start.getY() - end.getY());
        if (x + y == 1) {
            // check if this move will not result in the king
            // being attacked if so return true
            return true;
        }

        this.isValidCastling(board, start, end)
    }

    private def isValidCastling(Board board,Spot start, Spot end):Boolean= {

        if (this.isCastlingDone()) {
            return false;
        }

        // Logic for returning true or false
    }

    def isCastlingMove(Spot start, Spot end): Boolean = {
        // check if the starting and
    }
}

case class Queen(color:Color) extends Piece {

}

case class Knight(color: Color) extends Piece {
    override def canMove(Board board, Spot start,
                                            Spot end):Boolean = {
        // we can't move the piece to a spot that has
        // a piece of the same colour
        if (end.getPiece().isWhite() == this.isWhite()) {
            return false;
        }

        int x = Math.abs(start.getX() - end.getX());
        int y = Math.abs(start.getY() - end.getY());
        x * y == 2;
    }
}

case class Pawn(color: Color) extends Piece {

}

case class Move(player: Player, start: Spot, end:Spot,killedMove:Boolean = false) {
     val movedPiece = start.getPiece()
     val killedPiece:Option[Piece]=
     if(killedMove) {
        Option(end.getPiece())
     } else None

}

case class CastlingMove(player:Player, start: Spot,end: Spot) {
     val newStartSpot = Spot(start.row,start.col,end.getPiece())
     val newEndSpot =  Spot(end.row,end.col,start.getPiece())
}


case class Spot(row:Int,col:Int,piece: Option[Piece] = None)

trait Player {
   def color(): Color
   def isHuman():Boolean
}


trait GameStatus
object Active extends GameStatus
object BlackWin extends GameStatus
object WhiteWin extends GameStatus
object Forfeit extends GameStatus
object Stalemate extends GameStatus
object Resignation extends GameStatus

case class Computer(color:Color) extends Player {
   override isHuman(): Boolean = false
}
case class Human(color:Color) extends Player {
   override isHuman(): Boolean = true
}


cass Game {
private Player[] players;
    private var board:Board;
    private var currentTurn:Player;
    private var status:GameStatus;
    private var movesPlayed:List[Move];

    private def initialize(Player p1, Player p2): Unit={
        players[0] = p1;
        players[1] = p2;

        board.resetBoard();

        if (p1.isWhiteSide()) {
            this.currentTurn = p1;
        }
        else {
            this.currentTurn = p2;
        }

        movesPlayed.clear();
    }

    def boolean isEnd():Boolean = {
        return this.getStatus() != GameStatus.ACTIVE;
    }

    def boolean getStatus():Boolean = {
        return this.status;
    }

    def setStatus(GameStatus status):Unit= {
        this.status = status;
    }

    def playerMove(Player player, int startX,
                                int startY, int endX, int endY):Boolean = {
        Spot startBox = board.getBox(startX, startY);
        Spot endBox = board.getBox(startY, endY);
        Move move = new Move(player, startBox, endBox);
        return this.makeMove(move, player);
    }

    private def makeMove(Move move, Player player):Boolean= {
        Piece sourcePiece = move.getStart().getPiece();
        if (sourcePiece == null) {
            return false;
        }

        // valid player
        if (player != currentTurn) {
            return false;
        }

        if (sourcePiece.isWhite() != player.isWhiteSide()) {
            return false;
        }

        // valid move?
        if (!sourcePiece.canMove(board, move.getStart(),
                                            move.getEnd())) {
            return false;
        }

        // kill?
        Piece destPiece = move.getStart().getPiece();
        if (destPiece != null) {
            destPiece.setKilled(true);
            move.setPieceKilled(destPiece);
        }

        // castling?
        if (sourcePiece != null && sourcePiece instanceof King
            && sourcePiece.isCastlingMove()) {
            move.setCastlingMove(true);
        }

        // store the move
        movesPlayed.add(move);

        // move piece from the stat box to end box
        move.getEnd().setPiece(move.getStart().getPiece());
        move.getStart.setPiece(null);

        if (destPiece != null && destPiece instanceof King) {
            if (player.isWhiteSide()) {
                this.setStatus(GameStatus.WHITE_WIN);
            }
            else {
                this.setStatus(GameStatus.BLACK_WIN);
            }
        }

        // set the current turn to the other player
        if (this.currentTurn == players[0]) {
            this.currentTurn = players[1];
        }
        else {
            this.currentTurn = players[0];
        }

        true;
    }


}
