object NextClosestTime extends App {

  def nextClosestTime(time: String): String = {
    if (time == null || time.isEmpty) time
    else {
      var cur = time.substring(0,2).toInt * 60 + time.substring(3).toInt
      val allowed = time.filter(_ != ':').map( _.toInt - '0').toSet
      while(true){
        cur  = (cur + 1) % (24 * 60)
        val digits = List(cur/60 / 10, cur / 60 % 10, (cur % 60) / 10,(cur % 60) % 10 )
        var i = 0
        var error = false
        while(i < digits.size && !error){
          if(!allowed.contains(digits(i)))
            error = true
          i+= 1
        }
        if(!error) {
          val hours = cur / 60
          val minutes = cur % 60
          return f"$hours%02d:$minutes%02d"
        }
      }
      ""
    }
  }

  println(nextClosestTime("23:59"))
  println(nextClosestTime("19:34"))
}
