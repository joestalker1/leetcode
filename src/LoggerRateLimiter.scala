class Logger() {
  private var messageToTimestamp = Map.empty[String, Int]

  def shouldPrintMessage(timestamp: Int, message: String): Boolean = {
    val cur = messageToTimestamp.get(message)
    val shouldPrint = cur.map(tm => if (timestamp - tm >= 10) true else false).getOrElse(true)
    if (shouldPrint) messageToTimestamp = messageToTimestamp + (message -> timestamp)
    shouldPrint
  }

}
