import java.io.{StringWriter, File => JFile}
import java.io.BufferedWriter
import java.io.FileWriter
import scala.io.Source
import java.time.LocalDate

object TimeSeriesMerge extends App {

  implicit class RichString(val s: String) extends AnyVal {
    def asDate: LocalDate = LocalDate.parse(s)
  }

  class SelectableIterator(iter1: Iterator[String], iter2: Iterator[String])(select: (String, String) => String) extends Iterator[String] {
    private var line1: Option[String] = None
    private var line2: Option[String] = None

    override def hasNext: Boolean = iter1.hasNext || iter2.hasNext || line1.nonEmpty || line2.nonEmpty

    private def selectValue(): String = {
      val selected = line1.flatMap(s => line2.map(select(s, _))).get
      line1 = line1.filter(_ != selected)
      line2 = line2.filter(_ != selected)
      selected
    }

    private def getNonEmptyLeftovers(): String = {
      val selected = line2.orElse(line1).get
      if(line1.nonEmpty) line1 = None
      else line2 = None
      selected
    }

    override def next(): String = {
      if (line1.isEmpty && line2.isEmpty) {
        line1 = Option(iter1.next())
        line2 = Option(iter2.next())
        selectValue()
      } else if (line1.isEmpty || line2.isEmpty) {
        if(line1.isEmpty && iter1.hasNext) line1 = Option(iter1.next())
        if(line2.isEmpty && iter2.hasNext) line2 = Option(iter2.next())
        (for {
          _ <- line1
          _ <- line2
        } yield selectValue()).getOrElse(getNonEmptyLeftovers())
      } else selectValue()
    }
  }

  private def ifFileExists(fileName: String): Either[Throwable, JFile] = {
    val file = new JFile(fileName)
    if(!file.exists()) Left(new NoSuchElementException(s"Not found the file $file"))
    else Right(file)
  }

  def mergeTwoFiles(fileName1: String, fileName2: String): Either[Throwable, String] = {
    for {
      file1 <- ifFileExists(fileName1)
      file2 <- ifFileExists(fileName2)
      source1 = Source.fromFile(fileName1)
      source2 = Source.fromFile(fileName2)
    } yield {
      val resFileName = s"res${System.nanoTime()}"
      val writer = new BufferedWriter(new FileWriter(resFileName))
      for (line <- new SelectableIterator(source1.getLines, source2.getLines())((s1, s2) => if (s1.asDate.isBefore(s2.asDate)) s1 else s2)) {
        writer.write(line)
      }
      source1.close()
      source2.close()
      writer.close()
      resFileName
    }
  }

  def mergeFiles(fileNames:List[String]):String = {
    fileNames.reduce(mergeTwoFiles)
  }
}
