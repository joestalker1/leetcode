#LogisticsSystem
#Order
#Item
#User
#Vehicle
#Location
#PaymentDetails

class Location(country:String, state:String, district:String, street:String, building:String,flat:String, long:Long, lat:Long,)

class Item(name:String,width:Long,height:Long,length:Long,weightInKg: Int)

class Order(id:String, items:List[Item],date:Date,user:User, source:Location,destination:Location,paymentDetails: PaymentDetails,vehicle:Vehicle)

abstract class Vehicle(id: String,liftingCapacityInKg:Int,cargoHeight:Long,cargoWidth:Long,cargoLength:Long)

class Truck(id:String,orders:List[Order]) extends Vehicle {
    def addItem(item:Item):Boolean
    def removeItem(itemId: String):Unit
}
class Bike(id:String, order:Order) extends Vehicle{
   def addItem(item: Item):Boolean
    def removeItem(itemId: String):Unit
}

class User(firstName:String,lastName:String, email:String)


class LogisticsSystem(id:String,address:Location){

    def addUser(user:User) {

    }
    def orderDelivery(user,items:List[Items],fromSrc:Location,toDest:Location):List[Order] {
        val vehicles:List[Vehicle] = findVehicle()
        for (vehicle < - vehicles){
            val appenedeItems = new ListBuffer[Itme]
            for(item <- items){
               if(vehicle.addItem(item)){
                 appendedItems.add(item)
               }
            }
            order = createOrder(user,apppendItems,fromSrc,toSrc, vehicle)
        }
        return orders
     }
     def findVehicleByOrder(orderId: String)
     def findByOrder(orderId:String):Order
    findOrdersByDate(fromDate,endDate)
}



