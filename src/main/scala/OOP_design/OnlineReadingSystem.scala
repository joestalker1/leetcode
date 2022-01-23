case class Book{
  id:Long,
  title: String
  authors:List[Author]
}

case class Author{
  id:Long
  firstName:String
  lastName: String
}

case class User {
   id:Long,
   firstName:String
   lastName: String
   registerTime: Date
}

case class BookRegistry {
  def findByTitle(tile:String): List[Book]
  def findByAuthor(firstName:String,lastName:String): List[Book]
}

case class BookIssue {
  id:Long
  user:User
  book: Book
  fromData:Date
  lastDate: Date
}

case class Users {
   def add(user: User):Boolean
   def remove(id:Long):Boolean
   def find(firstName:String,lastName: String):List[User]
}

case class OnlineReadingSystem {
    //book API
    def findByTitle(tile: String): List[Book]
    def findByAuthor(firstName:String,lastName:String): List[Book]
    def giveBook(user:User, book:Book): BookIssue
    def isBookIssued(book:Book): Boolean
    //user API
    def add(user: User):Boolean
    def remove(id:Long):Boolean
    def find(firstName:String,lastName: String):List[User]
}