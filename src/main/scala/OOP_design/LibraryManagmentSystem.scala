

class BookFormat {
   val Hardcover,Audiobook,Paperback,Ebook,Newspaper,Magazine,Journal: Value
}
class BookStatus {
   val Available, Reserved,Loaned,Lost:Value
}
class ReservationStatus {
   Waiting,Pending,Completed,Canceled,None
}

class AccountStatus {
   Active,Closed,Canceled, Blacklisted,None
}

class Address{
   var streetAdress:String,
   var city:String,
   var zipCode:String,
   val country: String,
   val state: String
}
class Person {
   val name:String,
   val address: Address,
   val email:String,
   val phone: String
}
class Author{
   val name:String
   val description: String
   val books:List[Book]
}

class Book {
   val isbn:String,
   val title:String,
   val subject:String
   val publisher:String
   val language: String,
   val numberOfPages:Int
   val authors: List[Author]
}

class BookItem extends Book {
   val barcode: String,
   val isReferenceOnly: boolean,
   val borrowed: Date,
   val dueDate: Date,
   val price: Double,
   val format: BookFormat,
   val status: BookStatus,
   val dateOfPurchase: Date,
   val publicationDate: Date,
   val placeAt: Rack

  def checkout(String memberId): Bool = {
    if(bookItem.getIsReferenceOnly()) {
      ShowError("This book is Reference only and can't be issued");
      return false;
    }
    if(!BookLending.lendBook(this.getBarCode(), memberId)){
      return false;
    }
    this.updateBookItemStatus(BookStatus.LOANED);
    return true;
  }
}

class Rack {
  num: Int,
  locationIdf: String,
}

class Library {
  name: String,
  address: Address
  bookItems: List[BookItem]
}


class Account {
   val id:String,
   val status: AccountStatus,
   val person: Person,
   def resetPassword():Unit
}

class Librarian extends Account {
    def addBookItem(bookItem:BookItem):Unit
    def blockMember(acc:Account):Unit
    def unblockMember(acc:Account):Unit
}

class Member extends Account {
   val dateOfMember: Date,
   val totalBooksCheckedout: Int,

   def reserveBookItem(bookItem: BookItem):Unit

   private def incrementTotalBooksCheckedout()

   def checkoutBookItem(BookItem bookItem):Bool= {
    if (this.getTotalBooksCheckedOut() >= Constants.maxBooksIssuedToUser) {
      ShowError("The user has already checked-out maximum number of books");
      return false
    }
    val bookReservation = BookReservation.fetchReservationDetails(bookItem.getBarcode())
    if (bookReservation != null && bookReservation.getMemberId() != this.getId()) {
      // book item has a pending reservation from another user
      ShowError("This book is reserved by another member");
      return false;
    } else if (bookReservation != null) {
      // book item has a pending reservation from the give member, update it
      bookReservation.updateStatus(ReservationStatus.COMPLETED);
    }

    if (!bookItem.checkout(this.getId())) {
      return false;
    }

    this.incrementTotalBooksCheckedout();
    return true;
  }

  private def checkForFine(bookItemBarcode:String): Unit = {
    val bookLending = BookLending.fetchLendingDetails(bookItemBarcode);
    val dueDate = bookLending.getDueDate();
    val today = new Date();
    // check if the book has been returned within the due date
    if (today.compareTo(dueDate) > 0) {
      val diff = todayDate.getTime() - dueDate.getTime();
      val diffDays = diff / (24 * 60 * 60 * 1000);
      Fine.collectFine(memberId, diffDays);
    }
  }

  def returnBookItem(BookItem bookItem): Unit = {
    this.checkForFine(bookItem.getBarcode());
    val bookReservation = BookReservation.fetchReservationDetails(bookItem.getBarcode());
    if (bookReservation != null) {
      // book item has a pending reservation
      bookItem.updateBookItemStatus(BookStatus.RESERVED);
      bookReservation.sendBookAvailableNotification();
    }
    bookItem.updateBookItemStatus(BookStatus.AVAILABLE);
  }

  def renewBookItem(BookItem bookItem): Bool = {
    this.checkForFine(bookItem.getBarcode())
    val bookReservation = BookReservation.fetchReservationDetails(bookItem.getBarcode())
    // check if this book item has a pending reservation from another member
    if (bookReservation != null && bookReservation.getMemberId() != this.getMemberId()) {
      ShowError("This book is reserved by another member");
      member.decrementTotalBooksCheckedout();
      bookItem.updateBookItemState(BookStatus.RESERVED);
      bookReservation.sendBookAvailableNotification();
      return false;
    } else if (bookReservation != null) {
      // book item has a pending reservation from this member
      bookReservation.updateStatus(ReservationStatus.COMPLETED);
    }
    BookLending.lendBook(bookItem.getBarCode(), this.getMemberId());
    bookItem.updateDueDate(LocalDate.now().plusDays(Constants.maxLendingDays))
    return true;
  }
}

class LibraryCard {
   cardNumber: String,
   barcode: String,
   active: Bool,
   def isActive(): Bool
}

class BarcodeScanner {
   id: String,
   registeredAt: Date,
   active: Bool
}

class BookReservation {
   creationDate: Date,
   status: StatusReservation,
   def bookReservation(): ReservationStatus
}

object BookReservation {
   def fetchReservationDetails(String barcode):BookReservation;
}

public class BookLending {
  creationDate:Date;
  dueDate:Date
  returnDate:Date;
  bookItemBarcode:String;
  memberId: String;
  def lendBook(String barcode, String memberId): Bool
}

object BookLending {
    def fetchLendingDetails(String barcode):BookLending
}


public class Fine {
  val creationDate:Date;
  val bookItemBarcode: Double;
  val memberId:String;
}

object Fine {
    def collectFine(String memberId, long days):Unit
}

class FineTransaction {
   creationDate: Date,
   amount: Double
   def initiateTranscaction():Unit
}
class CreditCardTransaction extends FineTransaction {
   nameOnCard: String
}
class CheckTransaction extends FineTransaction {
   bankName : String,
   checkNumber: String
}
class CashTransaction extends FineTransaction {
   cashTendered: Double
}
trait Search {
  def searchByTitle(String title):List[Book]
  def searchByAuthor(String author):List[Book];
  def searchBySubject(String subject):List[Book]
  def searchByPubDate(Date publishDate): List[Book]
}


class Catalog extends Search {
   creationDate: Date,
   totalBooks: Int,
   totalTitles:Map[String, List[BookItem]]
   bookAuthors: Map[String, List[BookItem]]
   bookSubjects: Map[String, List[BookItem]]
   bookPublicationDates: Map[String,List[BookItem]]
   def updateCatalog():Unit
   def seachByTitle(s:String):List[BookItem]
   def searchByAuthor(s:String):List[BookItem]
   def searchBySubject(s: String): List[BookItem]
   def searchByPubDate(dt: Date): List[BookItem]
}

object Constants {
   val maxBooksIssuedToUser = 5
   val maxLendingDays = 10
}

