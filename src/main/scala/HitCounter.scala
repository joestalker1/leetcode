class HitCounter {
  private val elapsedPeriod = 300
  private val times = Array.ofDim[Int](elapsedPeriod)
  private val hits = Array.ofDim[Int](elapsedPeriod)

  /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
  def hit(timestamp: Int) {
    val index = timestamp % elapsedPeriod
    if(times(index) != timestamp){
      times(index) = timestamp
      hits(index) = 1
    } else hits(index) += 1
  }

  /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
  def getHits(timestamp: Int): Int = {
    times.zip(hits).filter(th => timestamp - th._1 < elapsedPeriod).map(_._2).sum
  }
}

object HitCounterApp extends App {
   val hitCounter = new HitCounter()
   hitCounter.hit(1)
   hitCounter.hit(2)
   hitCounter.hit(3)
   println(hitCounter.getHits(4))
   hitCounter.hit(300)
   println(hitCounter.getHits(300))
   println(hitCounter.getHits(301))
}