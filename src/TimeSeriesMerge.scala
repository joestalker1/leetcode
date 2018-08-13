import java.io.{StringWriter, File => JFile}
import java.io.BufferedWriter
import java.io.FileWriter
import scala.io.Source
import java.time.LocalDate

class StringMergableIterator(iter1: Iterator[String], iter2: Iterator[String])(select: (String, String) => String) extends Iterator[String] {
  private var line1: Option[String] = None
  private var line2: Option[String] = None

  override def hasNext: Boolean = iter1.hasNext || iter2.hasNext || line1.nonEmpty || line2.nonEmpty

  private def selectValue(): String = {
    val selectedOpt = for {
      s1 <- line1
      s2 <- line2
    } yield select(s1, s2)
    val selected = selectedOpt.fold(???)(identity)
    markAsUsed(selected)
    selected
  }

  private def markAsUsed(s:String):Unit = {
    line1 = line1.filter(_ != s)
    line2 = line2.filter(_ != s)
  }

  private def getNonEmptyLeftovers(): String = {
    val selectedOpt = line2.orElse(line1)
    if(line1.nonEmpty) line1 = None
    else line2 = None
    selectedOpt.fold("")(identity)
  }

  private def nextNonEmptyString(iter: Iterator[String]) = {
    if(iter.hasNext) {
      val s = iter.next().trim
      if(s.nonEmpty) Some(s) else None
    }
    else None
  }

  private def selectValueOrAnyNonEmpty():String = {
    (for {
      _ <- line1
      _ <- line2
    } yield selectValue).getOrElse(getNonEmptyLeftovers())
  }

  override def next(): String = {
    if (line1.isEmpty && line2.isEmpty) {
      if(iter1.hasNext) line1 = nextNonEmptyString(iter1)
      if(iter2.hasNext) line2 = nextNonEmptyString(iter2)
      selectValueOrAnyNonEmpty()
    } else if (line1.isEmpty || line2.isEmpty) {
      if(line1.isEmpty) line1 = nextNonEmptyString(iter1)
      if(line2.isEmpty) line2 = nextNonEmptyString(iter2)
      selectValueOrAnyNonEmpty()
    } else selectValue()
  }
}

object Utils {
  implicit class RichString(val s: String) extends AnyVal {
    def asDate: LocalDate = LocalDate.parse(s)
  }

  def ifFileExists(fileName: String): Either[Throwable, JFile] = {
    val file = new JFile(fileName)
    if(!file.exists()) Left(new NoSuchElementException(s"Not found the file $file"))
    else Right(file)
  }

  case class TextFile(fileName: String){
    private val writer = new BufferedWriter(new FileWriter(fileName))

    def writeln(s:String): Unit = {
      writer.write(s)
      writer.newLine()
    }

    def close(): Unit = writer.close()

    def path: String = fileName
  }

  def use[R](action: => R)(close: => Unit): R = try action finally close

  def extractPath(fileName: String): String = {
    val file = new JFile(fileName)
    val path = file.getAbsolutePath
    path.substring(0, path.lastIndexOf(JFile.separator))
  }

  def renameFile(oldName:String,newName:String):String = {
     val path = extractPath(oldName)
     val newPath = path + JFile.separator + newName
     (new JFile(oldName)).renameTo(new JFile(newPath))
     newPath
  }
}

import Utils._

object TimeSeriesMerge extends App {

  def takeMinDate(s1:String, s2:String):String = {
    val Array(date1, _) = s1.split("[ \t]")
    val Array(date2, _) = s2.split("[ \t]")
    if (date1.asDate.isBefore(date2.asDate)) s1 else s2
  }

  def mergeTwoFiles(fileName1: String, fileName2: String): Either[Throwable, String] = {
    for {
      _ <- ifFileExists(fileName1)
      _ <- ifFileExists(fileName2)
    } yield {
      val source1 = Source.fromFile(fileName1)
      val source2 = Source.fromFile(fileName2)
      val resFile = TextFile(extractPath(fileName1) + JFile.separator + s"result${System.nanoTime()}.txt")
      use {
        for (line <- new StringMergableIterator(source1.getLines, source2.getLines())(takeMinDate)) {
          resFile.writeln(line)
        }
      }{source1.close()
        source2.close()
        resFile.close()
      }
      resFile.path
    }
  }

  def mergeFiles(fileNames: List[String]): Either[Throwable, String] = {
    if(fileNames.isEmpty) Left(new Exception("List of files is empty"))
    else if(fileNames.size == 1) Right(fileNames.head)
    else {
      val firstFile:Either[Throwable, String] = Right(fileNames.head)
      val resFile = fileNames.tail.foldLeft(firstFile){(mayFileName, fileName) =>
        mayFileName.flatMap(mergeTwoFiles(_, fileName))
      }
      resFile.map { fn =>
        renameFile(fn, "result.txt")
      }
    }
  }


  val res = mergeFiles(List("/home/dfomenko/dev/projects/data/1.txt", "/home/dfomenko/dev/projects/data/2.txt",
    "/home/dfomenko/dev/projects/data/3.txt", "/home/dfomenko/dev/projects/data/4.txt"))
  println(res)
}
