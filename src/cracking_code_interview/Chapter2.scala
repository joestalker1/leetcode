package cracking_code_interview

class ListNode(var x: Int) {
  var next: ListNode = _
}

object Task2_1 extends App {
  def removeDups(list: ListNode): ListNode = {
    if (list == null) list
    else {
      var a = list
      while (a != null) {
        var b = a.next
        var prev = a
        while (b != null) {
          if (a.x == b.x) {
            prev.next = b.next
            prev = prev.next
          }
          b = b.next
        }
        a = a.next
      }
      list
    }
  }

  val a = new ListNode(0)
  a.next = new ListNode(1)
  a.next.next = new ListNode(1)
  a.next.next.next = new ListNode(3)
  val b = removeDups(a)
  println(b)
}

object Task2_2 extends App {
  def kthToLast(list: ListNode, k: Int): ListNode = {
    if (list == null) null
    else {
      var head = list
      var i = 0
      while (head != null && i < k) {
        head = head.next
        i += 1
      }
      var ptr = list
      while (ptr != null && head != null) {
        ptr = ptr.next
        head = head.next
      }
      ptr
    }
  }
}

object Task2_3 extends App {
  def deleteMiddle(list: ListNode): Unit = {
    if (list == null) ()
    else {
      var head = list
      var prev: ListNode = null
      while (head != null) {
        if (prev == null) prev = head
        else {
          //remove the middle node
          prev.next = head.next
          return
        }
      }
    }
  }
}

object Task2_4 extends App {
  def partition(list: ListNode, x: Int): ListNode = {
    if (list == null) list
    else {
      var head: ListNode = null
      var ptr = list
      var prev: ListNode = null
      while (ptr != null) {
        if (ptr.x < x) {
          //move a node to the front
          if (head == null) {
            head = ptr
            ptr = ptr.next
          }
          else {
            val t = ptr.next
            ptr.next = head
            head = ptr
            ptr = t
            if (prev != null) prev.next = t
          }
        }
        if (ptr.x >= x) prev = ptr
        ptr = ptr.next
      }
      head
    }
  }
}

//Task2_5 implemented

object Task2_6 extends App {
  private def lenOf(list: ListNode): Int = {
    if (list == null) 0
    else 1 + lenOf(list.next)
  }

  case class Part(s: String, isPoli: Boolean)

  private def traverse(list: ListNode, len: Int): Part = {
    if (list.next == null) { //last character
      Part("" + list.x.toChar, true)
    } else {
      val part = traverse(list, len)
      val half = if ((len & 0x1) == 1) (len - 1) / 2 else len / 2
      if (part.s.length < half) Part(list.x.toChar + part.s, true & part.isPoli)
      else if (part.s.length == half && (len & 0x1) == 1) part
      else Part(part.s.tail, part.s(0) == list.x.toChar && part.isPoli)
    }
  }

  def isPolyndrom(list: ListNode): Boolean = {
    if (list == null) false
    else {
      val len = lenOf(list)
      val res = traverse(list, len)
      res.s.isEmpty && res.isPoli
    }
  }
}

//Task2_7 implemented

object Task2_8 extends App {
  def isLoop(list: ListNode): Boolean = {
    if (list == null) false
    else {
      var head1 = list
      var head2 = list.next.next
      while (head1 != head2) {
        println(s"head1 ${head1.x}")
        println(s"head2 ${head2.x}")
        head1 = head1.next
        if (head2.next != null) head2 = head2.next.next
        else head2 = head2.next
      }
      println(s"${head1.x}")
      head1 != null && head1 == head2
    }
  }
  val list1 = new ListNode(1)
  list1.next = new ListNode(2)
  list1.next.next = new ListNode(3)
  list1.next.next.next = new ListNode(4)
  list1.next.next.next.next = list1 //new ListNode(5)
  //list1.next.next.next.next.next = list1
  println(isLoop(list1))

}