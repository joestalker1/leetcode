enum TransactionType {
  BalanceInquery,DepositCash,Withdraw,Transfer
}

enum TransactionStatus {
   Success,Failure,Blocked,Full,Partial,None
}

enum CustomerStatus {
   Active,Blocked,Banned,Compromised,Archived,Closed,Unknonw
}
class Address(streeAddress:String,city:String,state:String,zipcode:String,country:String)

class Bank {
   val account:Account
   val name:String,
   val bankCode:String
   def getBankCode():String
   def addATM():Boolean
}

class CashDispenser {
   val totalFiveDollarBills:Int
   val totalTwentyDollarBills:Int
   def dispenseCash(amount:Double):Int
   def canDispenseCash():Bool
}

class Keypad {
   def getInput():String
}
class Screen{
 def showMessage(msg:String):String
 def getInput():TransactionType
}
class Printer {
  def printRecept(trans:Transaction):String
}
class CardReader {
   def readCard():Boolean
}
class DepositSlot {
   val totalAmount:Double
   def getTotalAmount():Double
}
class CheckDepositSlot extends DepositSlot{
   def getCheckAmount():Double
}
class CashDepositSlot extends DepositSlot {
   def receiveDollarBills():Int
}
class Account {
  val accountNumber:Int
  val totalBalance:Double
  val availableBalance:Double
  def getAvailabeBalance():Double
}
class SavingAccount extends Account {
   def withdrawLimit():Bool
}
class CheckingAccount extends Account {
   def debitCardNumber():String
}
class Card {
   val cardNumber:String
   val customerName:String
   val canExpiry:Date
   val pin:Int
}
class ATM {
   val id:Int
   val location:Address
   val cashDispenser:CashDispenser
   val keypad:Keypad
   val screen:Screen
   val printer:Printer
   val cardReader:CardReader
   val checkDeposit:CheckDeposit
   val cashDeposit:CashDeposit

   def authenticateUser():Bool
   def makeTransaction(customer:Customer, transaction:Transaction):Boolean
}

class Customer {
   val name:String
   val email:String
   val phone:String
   val address:Address
   val status: CustomerStatus
   val card:Card
   val account:Account
   def makeTransaction(trans:Transaction):Boolean
   def getBillingAddress(): Address

}
class Transaction {
   val transId:Int
   val status: TransactionStatus
   val creationDate: Date
   def saveTransaction(): Boolean
}
class BalanceInquery extends Transaction{
   val accountId:Double
   def getAccount():Double
}
class Deposit extends Transaction {
  val amount:Double
  def getAmount(): Double
}
class Withdraw extends Transaction {
   val amount:Double
   def getAmount():Double
}
class Transfer extends Transaction {
    val destinationAccountNumber:Int
    val sourceAccountNumber:Int
    val amnount: Double
}
class CheckDeposit {
   val checkNumber:Int
   val bankCode: Int
}