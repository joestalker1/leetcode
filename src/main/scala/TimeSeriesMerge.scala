import java.io.{File => JFile}
import java.io.BufferedWriter
import java.io.FileWriter

import scala.io.Source
import java.time.LocalDate

import scala.concurrent.{Await, Future}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._

class StringSelectableIterator(iter1: Iterator[String], iter2: Iterator[String])(select: (String, String) => String) extends Iterator[String] {
  private var leftover1: Option[String] = None
  private var leftover2: Option[String] = None

  override def hasNext: Boolean = iter1.hasNext || iter2.hasNext || leftover1.nonEmpty || leftover2.nonEmpty

  private def selectString(): String = {
    val selected = (for {
      s1 <- leftover1
      s2 <- leftover2
    } yield select(s1, s2)).fold(???)(identity)
    markAsUsed(selected)
    selected
  }

  private def markAsUsed(s: String): Unit = {
    leftover1 = leftover1.filter(_ != s)
    leftover2 = leftover2.filter(_ != s)
  }

  private def getNonEmptyLeftovers(): String = {
    val selected = leftover2.orElse(leftover1).fold("")(identity)
    if (leftover1.nonEmpty) leftover1 = None
    else leftover2 = None
    selected
  }

  private def nextIfNotEmpty(iter: Iterator[String]) = {
    if (iter.hasNext) {
      val s = iter.next().trim
      if (s.nonEmpty) Some(s) else None
    }
    else None
  }

  private def selectStringOrLeftovers(): String = {
    (for {
      _ <- leftover1
      _ <- leftover2
    } yield selectString).getOrElse(getNonEmptyLeftovers())
  }

  override def next(): String = {
    if (leftover1.isEmpty || leftover2.isEmpty) {
      if (leftover1.isEmpty && iter1.hasNext) leftover1 = nextIfNotEmpty(iter1)
      if (leftover2.isEmpty && iter2.hasNext) leftover2 = nextIfNotEmpty(iter2)
      selectStringOrLeftovers()
    } else selectString()
  }
}

object Utils {

  implicit class RichString(val s: String) extends AnyVal {
    def asDate: LocalDate = LocalDate.parse(s)
  }

  case class TextFile(fileName: String) {
    private val writer = new BufferedWriter(new FileWriter(fileName))

    def writeln(s: String): Unit = {
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

  def renameFile(oldName: String, newName: String): String = {
    val path = extractPath(oldName)
    val newPath = path + JFile.separator + newName
    val newFile = new JFile(newPath)
    if (newFile.exists()) newFile.delete()
    (new JFile(oldName)).renameTo(newFile)
    newPath
  }
}

import Utils._

/**
  * Merges the files in the format: YYYY-MM-DD <number> by date in the increasing order.
  * The files should be sorted. The list of files should be passed in like <path1> <path2> ....
  * Records with same date value should be merged into one by summing up X values.
  * Resulting file will be stored in source directory with the name: result.txt.
  * Other files are just intermediate merging results.
  *
  */
object TimeSeriesMerge extends App {

  private def parseAndCompareDates(s1: String, s2: String): String = {
    val date1 = parseDate(s1)
    val date2 = parseDate(s2)
    if (date1.isBefore(date2)) s1 else s2
  }

  private def parseDate(s: String): LocalDate = {
    val Array(subs, _) = s.split("[ \t]")
    subs.asDate
  }

  private def parseInt(s: String): Int = {
    val Array(_, a) = s.split("[ \t]")
    a.toInt
  }

  private def mergeTwoFiles(fileName1: String, fileName2: String): String = {
    val source1 = Source.fromFile(fileName1)
    val source2 = Source.fromFile(fileName2)
    val resFile = TextFile(extractPath(fileName1) + JFile.separator + s"result${System.nanoTime()}.txt")
    use {
      for (line <- new StringSelectableIterator(source1.getLines, source2.getLines())(parseAndCompareDates)) {
        resFile.writeln(line)
      }
    } {
      source1.close()
      source2.close()
      resFile.close()
    }
    resFile.path
  }


  def mergeFiles(fileNames: Array[String], from: Int, to: Int): Future[String] = {
    if ((to - from + 1) == 2) {
      //can merge two 2 files
      Future(mergeTwoFiles(fileNames(from), fileNames(to)))
    } else {
      val mid = from + (to - from) / 2
      val merged1 = mergeFiles(fileNames, from, mid)
      val merged2 = mergeFiles(fileNames, mid + 1, to)
      merged1.flatMap { fileName1 => merged2.map(mergeTwoFiles(fileName1, _)) }
    }
  }

  private def reduceBy(fileName: String): String = {
    val source = Source.fromFile(fileName)
    val resFile = TextFile(extractPath(fileName) + JFile.separator + s"result${System.nanoTime()}.txt")
    use {
      var last = ""
      var lastDate: LocalDate = null
      var acc: Int = 0
      for (line <- source.getLines) {
        val date = parseDate(line)
        if (last.isEmpty || date != lastDate) {
          if (lastDate != null && date != lastDate) resFile.writeln(s"$lastDate $acc")
          last = line
          lastDate = parseDate(last)
          acc = parseInt(last)
        } else {
          val a = parseInt(line)
          acc += a
        }
      }
      //append the last sting
      if (last.nonEmpty) resFile.writeln(s"$lastDate $acc")
      resFile.path
    } {
      source.close()
      resFile.close()
    }
  }

  if (args.isEmpty) println("Define the list of files for merging")
  else {
    val strings = if (args.size == 1) args.flatMap(_.split("[ \t]")) else args
    val res = Await.result(mergeFiles(strings, 0, strings.length - 1).map(fn => renameFile(reduceBy(fn), "result.txt")), 10 minutes)
    println(res)
  }
}
