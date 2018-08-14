package src

import java.io.{BufferedWriter, FileWriter, File => JFile}

object DataGenerator extends App {
  case class TextFile(fileName: String){
    private val writer = new BufferedWriter(new FileWriter(fileName))

    def writeln(s:String): Unit = {
      writer.write(s)
      writer.newLine()
    }

    def close(): Unit = writer.close()

    def path: String = fileName
  }

  val path = "/home/dfomenko/dev/projects/data"

   for (i <- 0 to 5){
      val fileName = path + JFile.separator + s"$i.txt"
      val textFile = TextFile(fileName)
      val rnd = new scala.util.Random
      for(year <- 1 to 9999) {
        val num = rnd.nextInt()
        val data = f"$year%04d-01-01 $num"
        textFile.writeln(data)
      }
      textFile.close()
   }

}
