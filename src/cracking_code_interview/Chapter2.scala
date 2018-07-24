package cracking_code_interview

class ListNode {
  var next: ListNode = _
  var x: Int = 0
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

  val a = new ListNode()
  a.x = 0
  a.next = new ListNode()
  a.next.x = 1
  a.next.next = new ListNode()
  a.next.next.x = 1
  a.next.next.next = new ListNode()
  a.next.next.next.x = 3
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
  def deleteMiddle(list:ListNode):Unit = {
    if(list == null) ()
    else{
      var head = list
      var prev:ListNode = null
      while(head != null){
        if(prev == null) prev = head
        else{
          //remove the middle node
          prev.next = head.next
          return
        }
      }
    }
  }
}

object Task2_4 extends App {
  def partition(list:ListNode,x:Int):ListNode = {
    if(list == null) list
    else{
      var head:ListNode = null
      var ptr = list
      var prev:ListNode = null
      while(ptr != null){
        if(ptr.x < x){
          //move a node to the front
          if(head == null) {
            head = ptr
            ptr = ptr.next
          }
          else {
            val t = ptr.next
            ptr.next = head
            head = ptr
            ptr = t
            if(prev !=null) prev.next = t
          }
        }
        if(ptr.x >= x) prev = ptr
        ptr = ptr.next
      }
      head
    }
  }
}
//Task2_5 implemented
object Task2_6 extends App {
//  private def lenOf(list:ListNode): Int = {
//    if(list == null) 0
//    else 1 + lenOf(list.next)
//  }
//
//  private def isPolyndrom(list:ListNode): Boolean = {
//
//  }
//
//
//  def isPolyndrom(list:ListNode): Boolean = {
//
//  }
}