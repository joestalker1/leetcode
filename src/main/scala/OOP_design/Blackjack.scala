class Person {
  val name:String,
  val address:Address,
  val email:String,
  val phone:String
}
enum Suit {
   Heart,Spade,Club,Diamond
}
enum AccountStatus {
   Active,Closed,Canceled,Blacklisted,None
}
class Game {
  val player:Player
  val Dealer dealer:Dealer;
  val shoe:Shoe;
  val MAX_NUM_OF_DECKS = 3;

  def playAction(string action, Hand hand): Unit = {
    switch(action) {
      case "hit": hit(hand); break;
      case "split": split(hand); break;
      case "stand pat": break; //do nothing
      case "stand": stand(); break;
      default: print("Wrong input");
    }
  }

  def hit(Hand hand):Unit = {
    hand.addCard(shoe.dealCard())
  }

  def stand(): Unit = {
    val dealerScore = dealer.getTotalScore()
    val playerScore = player.getTotalScore()
    val hands = player.getHands()
    for(Hand hand <- hands) {
      val bestScore = hand.resolveScore()
      if(playerScore == 21){
        //blackjack, pay 3:2 of the bet
      } else if (playerScore > dealerScore) {
        // pay player equal to the bet
      } else if (playerScore < dealerScore) {
        // collect the bet from the player
      } else { //tie
        // bet goes back to player
      }
    }
  }

  def split(Hand hand):Unit = {
    val cards = hand.getCards();
    player.addHand(new Hand(cards[0], shoe.dealCard()))
    player.addHand(new Hand(cards[1], shoe.dealCard()))
    player.removeHand(hand)
  }


 def thi(Player player, Dealer dealer) {
    this.player = player
    this.dealer = dealeer
    Shoe shoe= new Shoe(MAX_NUM_OF_DECKS)
  }

  def start():Unit = {
    player.placeBet(getBetFromUI())
    val playerHand = new Hand(shoe.dealCard(), shoe.dealCard())
    player.addToHand(playerHand)

    val dealerHand = new Hand(shoe.dealCard(), shoe.dealCard())
    dealer.addToHand(dealerHand)

    while(true){
      val hands = player.getHands()
      for(Hand hand <- hands) {
        val action = getUserAction(hand)
        playAction(action, hand)
        if(action.equals("stand")) {
          break
        }
      }
    }
  }

  public static void main(String args[]) {
    Player player = new Player();
    Dealer dealer = new Dealer();
    Game game = new Game(player, dealer);
    game.start();
  }
}

class Deck {
   val createdOn:Date
   def getCard():List[BlackjackCard]

}
class Player extends BasePlayer{
   val bet:Int
   val totalCash:Int
   def getHands():Hand
   def removeHands():Bool
}
class BasePlayer {
    val id:String
    val pass:Password
    val balance:Int
    val status:AccontStatus
    val person:Person
    val hands:List[Hand]
    def resetPassword():Bool
}
class GameView{
   def playAction():Bool
}
class GameContoroller {
   def validateAction():Bool
}

class Shoe {
   val List<BlackjackCard> cards:List[BlackjackCard]
   val numberOfDecks:Int;

  def createShoe() {
     val cards =new ListBuffer[BlackjackCard]()
     for(i <- 0 to numberOfDecks) {
        cards.add((new Deck()).getCards())
     }
  }


  def this(int numberOfDecks: Int) {
    this.numberOfDecks = numberOfDecks
    createShoe()
    shuffle()
  }

  def shuffle(): Unit {
    val cardCount = cards.size()
    val r = new Random();
    for(i <- 0 to cardCount) {
       val index = r.nextInt(cardCount - i - 1);
       swap(i,index)
    }
  }

  def swap(int i, int j): Unit= {
    val temp = cards(i)
    cards(i) = cards(j)
    cards(j) = temp
  }

  //Get the next card from the shoe
  def dealCard():BlackjackCard = {
    if(cards.size() == 0 ){
      createShoe()
    }
    cards.remove(0)
  }
}
class BlackjackCard extends Card {
  def this(suit:Suit, faceValue:Int) {
    this.gameValue = faceValue
    if(this.gameValue > 10)
      this.gameValue = 10;
   }

   val gameValue:Int
  def getGameValue():Int
}
class Card {
    val suite:Suite
    val faceValue:Int
    def getFaceValue():Int
}

class Hand {
  val cards:List[BlackjackCard]

  def getScores():List[Int] = {
    val totals = new ArrayList()
    total.add(0)

    for (card <- cards) {
      val newTotals = new ArrayList()
      for (int score <- totals) {
        newTotals.add(card.faceValue() + score);
        if (card.faceValue() == 1) {
          newTotals.add(11 + score)
        }
      }
      totals = newTotals
    }
    totals
  }

  def this(c1:BlackjackCard, c2:BlackjackCard) {
    this.cards = new ListBuffer<BlackjackCard>()
    this.cards.add(c1)
    this.cards.add(c2)
  }

  def addCard(BlackjackCard card): Unit = {
    cards.add(card)
  }

  // get highest score which is less than or equal to 21
  defresolveScore() : Int= {
    val scores = getScores()
    val bestScore = 0
    for (int score <- scores) {
      if (score <= 21 && score > bestScore) {
        bestScore = score
      }
    }
    bestScore
  }

}