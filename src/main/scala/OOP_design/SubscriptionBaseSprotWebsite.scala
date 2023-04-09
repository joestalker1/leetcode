enum GameStatus {
  Win,Loss,Draw
}

enum AccountStatus {
   Active,Deleted,OnHold
}

enum SportKind {
 Socker,Tennis,HourseRiding,Swimming
}

class Score {
   val count:Int
   val when: DateTime
   val comment: String
}
class Game {
  val name:String
  val happendAt:DateTime
  val sportKind:SportKind
  val scores:List[Score]
  val status: GameStatus
}
class Subscription {
   val id:String
   val sportKinds: List[SportKind]
   val expiredAt:DateTime
   val createdAt: DateTime

   def stop():Boolean
   def delete():Boolean
}

class History {
   val id: String
   val games: List[Game]
}

class Guest {
  def register():Unit
}

class Account {
   val id:String
   val createdAt:DateTime
   val account:AccountStatus
}

class Member extends Guest {
   val id:String
   val name:String
   val createdAt: DateTime
   val accountStatus: AccountStatus
   val subcription:List[Subscription]
   def addSubcription(subcription:Subscription): Boolean
}

class Admin extends Guest {
   def addMember(member:Member):Boolean
   def deleteMembr(member: Member): Boolean
}

trait System {
 def subscribe(member: Guest):Boolean
 def unsubscrive(member: Guest): Boolean
 def findHistory(member:Guest):List[History]
}

