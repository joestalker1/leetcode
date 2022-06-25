
object ParkingSpotType {
  val Handiccaped,
  Motorbike,
  Large,
  Compact,
  Electric
}

object VehicleType {
 Car,Truck,Electric, Van
}

object ParkingTicketStatus {
  Active,Paid,Lost
}

object AccountStatus {
  Active,Closed,Canceled, Blacklisted,None
}

class Location(streetAddress:String, city:String, state:String,zipcode:String, country:String)

class Person(name:String, address:Location,email:String, phone:String)

class ParkingRate(hourNumber:Int, rate:Double)

class ParkingLot(name:String, address:Location, parkingRate:ParkingRate,compactSpotCount:Int,largeSpotCount:Int,
      motorbikeSpotCount:Int,electricSpotCount:Int,maxCompactCount:Int, maxLargeCount:Int,maxMotorbikeCount:Int,
      maxElectricCount:Int,entrancePanels:Map[String, EntrancePanel],exitPanels: Map[String, ExitPanel],
         parkingFloors:Map[String, ParkingFloor],activeTickets: Map[String, ParkingTicket]) {

   def addParkingFloor():Boolean
   def addEntrancePanel():Unit
   def isFull(type: VehicleType):Boolean
   def getNewParkingTicket(Vehicle vehicle): ParkingTicket
   def isFull():Boolean
   def addParkingFloor(floor: ParkingFloor):Unit
   def addEntrancePanel(entrancePanel:EntrancePanel): Unit
   def addExitPanel(exitPanel: ExitPanel):Unit
}

class ParkingFloor(name: String,handicappedSpots:Map[String, HandicappedSpot],compactSpots:Map[String, CompactSpot],
       largeSpots:Map[String, LargeSpot], motorbikeSpots:Map[String, MotorbikeSpot],
        electricSpots:Map[String, ElectricSpot], infoPortals:Map[String, CustomerInfoPortal], displayBoard:ParkingDisplayBoard) {
  def updateDisplayBoard()
  def addParkingSpot(spot:ParkingSpot)
  def assignVehicleToSpot(vehicle:Vehicle, spot:ParkingSpot):Unit
  def freeSpot(spot:ParkingSpot): Unit
}

class ParkingDisplayBoard(id:String,handiccapedFreeSlot: HandicappedSlot,compactFreeSlot:LargeSlot,
motorbikeFreeSlot:MotorbikeSlot,electricFreeSlot:ElectricSlot) {
  def showEmptySpotNumber()
}

sealed trait ParkingSpot(number:String,free:Boolean,type:ParkingSlotType,vehicle:Vehicle,getIsFree: Boolean){
  def assignVehicle(Vehicle vehicle):Unit
  def removeVehicle():Boolean
  def isFree:Boolean
}

class HandiccapedSpot() extends ParkingSpot
class CompactSpot() extends ParkingSpot
class LargeSpot() extends ParkingSpot
class MotorbikeSpot() extends ParkingSpot
class ElectricSpot() extends ParkingSpot

class ElectricPanel1(payedForMinutes:Int,chargingStartTime:DateTime){
  def cancelCharging():Boolean
}

class ElectricPanel2(id:String) {
  def printTicket():Unit
}

class ExitPanel(id:String) {
   def scanTicket():Unit
   def processPayment():Unit
}

class ParkingAttendantPortal(id:String){
  def scanTicket():Boolean
  def processPayment():Unit
}
class CustomerInfoPortal(id:String) {
    def scanInfoPanel():Boolean
    def processPayment():Boolean
}

class Vehicle(licenseNumber: String,type: VehicleType,ticket:ParkingTicket) {
    def assignTicket(ticket:ParkingTicket):Unit
}

class Car extends Vehicle
class Truck extends Vehicle
class Electric extends Vehicle
class Van extends Vehicle
class Motorbike extends Vehicle

class Account(user:String,pass:String,status: AccountStatus) {
 def resetPassword():Unit
}

class Admin extends Account {
  def addParkingFloor(floor:ParkingFloor):Boolean
  def addParkingSpot(floorName:String, spot:ParkingSpot):Boolean
  def addParkingDisplayBoard(floorName:String, displayBoard:ParkingDisplayBoard):Boolean
  def addCustomerInfoPanel(floorName:String, infoPanel:CustomerInfoPanel):Boolean

  def addEntrancePanel(entrancePanel:EntrancePanel): Boolean
  def addExitPanel(exitPanel: ExitPanel): Boolean
}

class ParkingAttendant extends Account {
    def processTicket(string ticketNumber:String):Unit
}

class ParkingTicket(ticketNum:String,issuedAt:DateTime, payedAt:DateTime,payedAmount:Double,status: ParkingTicketStatus)

class Payment(creationDate:Date,amount:Double, status: PaymentStatus) {
   def initiateTransaction(): Boolean
}

class CreditCardTransaction extends Payment
class CashTransaction extends Payment