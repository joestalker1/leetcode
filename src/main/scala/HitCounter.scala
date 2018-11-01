class HitCounter {
  private val elapsedPeriod = 300

  /** Initialize your data structure here. */
  private var buffer = Array.ofDim[Int](32)
  private var size  = 0

  /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
  def hit(timestamp: Int) {
     size += 1
     if(size == buffer.length) {
       val old = buffer
       buffer = Array.ofDim[Int](buffer.size * 2)
       old.copyToArray(buffer)
     }
     buffer(size - 1) = timestamp
  }

  /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
  def getHits(timestamp: Int): Int = {
     val start = timestamp - elapsedPeriod
     if(start <= 0) buffer.size
     else {
        var i = 0
        while(i < buffer.size && buffer(i) <= start) i += 1
        buffer.size - i
     }
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