case class Address(street:String,city:String,state:String,zipcode:String,country:String)

object OrderStatus extends Enumeration {
  val Unshipped,Pending,Completed,Canceled,RefundApplied
}

object AccountStatus {
 Active,Blocked,Banned,Compromised,Archived,Uknown
}

object ShippmentStatus {
  Pending,Shipped, Delivered,OnHold
}

object PaymentStatus {
   Unpaid, Pending,Completed,Failed,Decline,Canceled,Abandoned,Settled, Refunded
}

case class Account(user:String,pass:String,status: PaymentStatus,name:String,shippingAddress:Address,email:String,phone:String) {

  val creditCards: List[CreditCard];
  val bankAccounts:List[ElectronicBankTransfer];

  public def addProduct(Product product:Product):Boolean
  public def addProductReview(review: ProductReview):Boolean
  public def resetPassword():Boolean
 def addProductReview():Unit
 def addProduct():Unit
}

case class CreditCard(name:String,cardNum:Integer,code:Int,billingAddress:Address)

case class ElectronicBankTransfer(bank:String,routingNum:String,accountNum:String)

abstract class Customer{
  val cart:ShoppingCart;
  val order:Order;

  def getShoppingCart():ShoppingCart;
  def addItemToCart(Item item):Boolean;
  def removeItemFromCart(Item item):Boolean;
  def getShoppingCard():ShoppingCard
}
public class Guest extends Customer {
  def registerAccount():Boolean;
}

public class Member extends Customer {
  val account:Account;
  def placeOrder(Order order):OrderStatus;
}

case class Admin() extends Customer {
  def blockUser():Unit
  def addNewProductCategory():Unit
  def modifyProductCategory():Unit
}

abstract class Payment {
   val status: PaymentStatus
   amount: Double

   def processPayment:PaymentStatus
}

case class ElectronicBankTransfer extends Payment
case class CreditCardTransaction extends Payment

case class ShoppingCart(items:List[Item]) {
  def addItem(Item item):Item
  def removeItem(Item item):Boolean
  def updateItemQuantity(Item item, int quantity)
  def public List<Item> getItems():List[Item]
  def checkout():Boolean
}

case class Item(qnt:Int,price:Double) {
   val productID:String;
   public def updateQuantity(int quantity):Boolean;
}

case class Order(num:String,status:OrderStatus,orderDate:Date){
  val orderLog:List[OrderLog]

  def sendForShipment():Boolean
  def makePayment(Payment payment):Boolean
  def addOrderLog(OrderLog orderLog):Boolean
  def sendForShippment()
}

case class OrderLog(num:String,creationDate:Date,status: OrderStatus) {
}

case class Catalog(name:String, product:Map[String,List[Product]]) {
  def lastUpdate():Date
  def productCategories:Map[String,List[Product]]
}

case class Product(productId:String,name:String, description:String,price:Double,avalCnt:Int,category:ProductCategory){

  val seller:Account

  def getAvailableCount():Int
  def updatePrice(double newPrice):Boolean
   def avalCount():Int
}

case class ProductCategory(name:String, desc:String)

public class ProductReview {
  val rating:Int;
  val review:String;

  val reviewer:Member;
}

case class Shipment {
  val shipmentNumber:String
  val shipmentDate: Date
  val estimatedArrival:Date
  val shipmentMethod:String;
  val shipmentLogs:List[ShipmentLog]

  def addShipmentLog(ShipmentLog shipmentLog):Boolean
  def addShipmentLog():boolean
}

case class ShipmentLog {
  val shipmentNumber:String
  val status:ShipmentStatus
  val creationDate:Date

}

case class ProductReview(rating:Int,review:String){
  def getRating():Int
}

abstract class Notification {
   val notificationId:String
   val createdOn:Date
   val content:String

   def sendNotification(acc:Account):Bool
}

case class SmsNotification(phone:String) extends Notification

case class EmailNotification(email:String) extends Notification

trait Search {
  def searchProductsByName(String name): List[Product]
  def searchProductsByCategory(String category):List[Product]
}

class Catalog extends Search {
   val productNames:HashMap[String, List[Product]];
   val productCategories: HashMap[String, List[Product]]

  public def searchProductsByName(String name):List[Product] {
      productNames(name)
  }

  def searchProductsByCategory(String category): List[Product] {
     productCategories(category)
  }
}