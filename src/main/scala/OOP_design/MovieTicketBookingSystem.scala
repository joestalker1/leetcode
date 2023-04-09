class Address{
   val streetAddress:String
   val city:String
   val state: String
   val zipCode:String
   val country:String
}

enum BookingStatus {
    Requested,Pending,Confirmed,Checked-in,Canceled,Abandoned
}

enum SeatType {
   Regular,
   Premium,
   Accessable,
   EmergencyExit,
   Other
}
enum AccountStatus {
   Active,
   Closed,
   Canceled,
   Blacklisted,
   Blocked
}

enum PaymentStatus {
   Unpaid,Pending,Completed,Failed,Declined,Canceled,Abandoned,Settling,Settled,Refunded
}
trait Search {
 def searchByTitle(title:String)
 def searchByLang(lang:String)
 def searchByGenre(genre:String)
 def searchByReleaseDate(date:Date)
 def searchByCity(name:String)
}

class Catalog extends Search {
  val lastUpdate:Date
  val movieTitle:Map[String,List[Movie]]
  val movieLang:Map[String,List[Movie]]
  val movieGenres:Map[String,List[Movie]]
  val movieReleaseDate:Map[String,List[Movie]]
  val movieCities:Map[String,List[Movie]]
}
class Movie {
   val title:String,
   val desc:String,
   val durationMins:Int,
   val lang: String,
   val releaseDate:Date,
   val country:String,
   val shows:List[Show]
}
class Show {
 val createdOn:Date,
 val startTime: Date,
 val endTime:Date
}
class Cinema{
   val name:String,
   val totalCinemaHalls: Int,
   val location:Location
   val halls:List[CinemaHall]
}

class CinemaHall{
  val name:String
  val totalSeats:Int
  val seats: List[CinemaHallSeat]
  val show:List[Show]
}

class CinemaHallSeat{
   val seaRow:Int
   val seatColumn:Int
   val type:SeatType
}
class City{
   val name:String,
   val state:String,
   val zipCode:String

}
class Account {
   val id:String
   val password:String
   val status:AccountStatus
   def resetPassword():Unit
}

class Guest{
  def registerAccount():Unit
}
class Person {
    val name:String
    val address:Address
    val email:String
    val phone:String
    val account:Account
}

class Admin extends Person{
  def addMovie(movie:Movie):Bool
  def addShow(show:Show):Bool
  def blockUser(customer:Customer):Bool
}
class Customer extends Person {
   def makeBooking():Bool
   def getBooking():List[Booking]
}

class FrontDeskOfficer extends Person {
    def createBooking(booking:Booking):Bool
}

class Booking {
   val bookingNum:String
   val numOfSeats:Int
   val createOn:Date
   val status:BookingStatus
   val seats:List[ShowSeat]
   val show:Show
   val payment:Payment

   def makePayment(payment:Payment):Bool
   def cancel():Bool
   def assignSeats(seats:List[ShowSeat]):Bool
}

class ShowSeat extends CinemaHallSeat{
  val seatNum:Int
  val isReserved:Bool
  val price:Double
}
class Payment{
  val amount:Double
  val createdOn:Date
  val status:PaymentStatus
  val transId:Int
}
class CreditCardTransaction extends Payment{
    val nameOnCard:String
}
class CashTransaction extends Payment {
   val cashTendered:Double
}
class Coupon {
   id:Int
   val balance:Double
   val expiry:Date
}
class Notification {
   val id:Int
   val createdOn:Date
   val content:String
   def sendNotification():Bool
}

class EmailNotification extends Notification {
   email:String
}
class SmsNotification extends Notification {
    phone:String
}
