enum QuestionStatus {
    Open,Close,OnHold,Deleted
}

enum QuestionClosingRemark {
   Duplicate,Offtopic,Tooboard,NotConstructive,NotRealQuestion,PrimaryOpinionBased
}

enum AccountStatus {
   Active,Blocked,Banned, Compromised,Archived,Uknown
}

class Guest {
  def registerAccount():Boolean
}

class Account {
   val id:String
   val status: AccountStatus
   val name:String
   val email: String
   val phone: String
   val reputation: Int

   def resetPassword():Unit
}

class Badge {
 val name:String
 val desc: String
}

class Member {
    val account Account
    val badges: List[Badges]
    def getReputaion():Int
    def getEmail():String
    def createQuestion(q:Question): Boolean
    def createTag(tag: Tag): Boolean
}

class Admin extends Member {
   def blockMember(member: Member):Boolean
   def unlockMemnber(member: Member): Boolean
}

class Moderator extends Member {
   def closeQuestion(q:Question):Boolean
   def undeleteQuestion(q:Question):Boolean
}

class Comment{
  val text: String
  val createdAt: Long
  val flagCount: Int
  val voteCount: Int
  val askingMember: Member
}

class Photo {
   val photoId:String
   val photoPath:String
   val createdAt:Long
   def delete():Unit
}
class Answer {
   val comments:List[Comment]
   val photos: List[Photo]
   val answerText: String
   val accepted: Boolean
   val voteCount:Int
   val flagCount:Int
   val createdAt: Long
   val creatingMember: Member;
   def incrementFlagCount():Int
}

class Notification {
   val notificationId:Int
   val createdOn: Long
   val content: String

   def sendNotification(): Boolean
}

class Bounty {
   val reputation: Int
   val expiredAt: Long
   def modifyReputation():Unit
}
trait Search {
   def search(query:String): List[Question]
}

class Question extends Search {
   val bounty:List[Bounty]
   val photos:List[Photo]
   val answer: List[Answer]
   val comments: List[Comment]
   val title:String
   val desc: String
   val viewCount:Int
   val voteCount:Int
   val createAt:Long
   val updateAt:Long
   val status: QuestionStatus
   val closingRemark: QuestionClosingRemark
   def close():Boolean
   def undelete():Boolean
   val askingMember: Member
   val bounty: Bounty

   def close():Boolean
   def undelete():Boolean
   def addComment(c:Comment): Boolean
   def addBounty(b:Bounty): Boolean

   def search(q:String): List[Question] = {}
}

class Tag{
 val name:String
 val desc: String
 val dailyAskedFreq:Int
 val weeklyAskedFreq: Int
}