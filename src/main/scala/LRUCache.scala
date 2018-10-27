object LRUCache {
  case class Entry(key: Int, value: Int, var before: Entry, var after: Entry)
}

import LRUCache._

class LRUCache(_capacity: Int) {
  private var underlaying = Map.empty[Int, Entry]
  private var head: Entry = null
  private var tail: Entry = null //most youngest item in cache

  def get(key: Int): Int = {
    val ifEntry = underlaying.get(key)
    ifEntry.map { entry =>
      addToEnd(entry)
      entry.value
    }.getOrElse(-1)
  }

  private def addToEnd(entry: Entry): Unit = {
    if (head == entry) {
      if (tail != entry) {
        head = entry.after
        if (entry.after != null) {
          entry.after.before = null
        }
      }
    } else if (tail != entry) { // entry in the middle
      val b = entry.before
      b.after = entry.after
      entry.after.before = b
    }
    if (tail != entry) {
      entry.after = null
      entry.before = null
      linkNodeLast(entry)
    }
  }

  private def unlinkNode(node: Entry): Unit = {
     if(head == node){
       if(tail == node){
         head = null
         tail = null
       } else {
         val p = node.after
         p.before = null
         head = p
       }
     } else if(tail == node) {
        val p = node.before
        p.after = null
        tail = p
     } else {
       val p = node.before
       p.after = node.after
       node.after.before = p
     }
     node.after = null
     node.before = null
  }

  def put(key: Int, value: Int) {
    if(underlaying.exists(_._1 == key)) unlinkNode(underlaying(key))
    else if (underlaying.size == _capacity) evictOldest()
    val entry = Entry(key, value, null, null)
    underlaying = underlaying + (key -> entry)
    linkNodeLast(entry)
  }

  private def linkNodeLast(p: Entry): Unit = {
    val last = tail
    tail = p
    if (last == null)
      head = p
    else {
      p.before = last
      last.after = p
    }
  }

  private def evictOldest(): Unit = {
    val h = head
    if(h == tail){
      head = null
      tail = null
    } else {
      head = h.after
      h.after.before = null
    }
    h.after = null
    h.before = null
    underlaying = underlaying - h.key
  }

}

//["LRUCache","get","put","get","put","put","get","get"]
//[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
object LRUApp extends App {
  val cache = new LRUCache(2)
  println(cache.get(2))
  cache.put(2,6)
  println(cache.get(1))
  cache.put(1, 5)
  cache.put(1, 2)
  println(cache.get(1))
  println(cache.get(2))

//  val cache = new LRUCache(1)
//  cache.put(2, 1)
//  println(cache.get(2))
//  cache.put(3, 2)
//  println(cache.get(2))
//  println(cache.get(3))

  //  cache.put(2, 2)
  //  println(cache.get(1))       // returns 1
  //  cache.put(3, 3)    // evicts key 2
  //  println(cache.get(2))       // returns -1 (not found)
  //  cache.put(4, 4)    // evicts key 1
  //  println(cache.get(1))       // returns -1 (not found)
  //  println(cache.get(3))       // returns 3
  //  println(cache.get(4))       // returns 4
}

//["LRUCache","put","get","put","get","get"]
//[[1],[2,1],[2],[3,2],[2],[3]]