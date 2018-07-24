object Solution extends App {

  class ListNode(var x: Int) {
    next = null
    var next: ListNode = null
  }


  private def mergeTwoLists(list1: ListNode, list2: ListNode): ListNode = {
    var l1 = list1
    var l2 = list2
    var head: ListNode = null
    var tail: ListNode = null
    while (l1 != null && l2 != null) {
      if (l1.x == l2.x) {
        if (head == null) {
           head = new ListNode(l1.x)
           head.next = new ListNode(l2.x)
           tail = head.next
        } else {
          tail.next = new ListNode(l1.x)
          tail.next.next = new ListNode(l2.x)
          tail = tail.next.next
        }
        l1 = l1.next
        l2 = l2.next
      } else {
        if(l2.x < l1.x) {
          val temp = l1
          l1 = l2
          l2 = temp
        }
        if (head == null) {
           head = new ListNode(l1.x)
           tail = head
        } else {
          tail.next = new ListNode(l1.x)
          tail = tail.next
        }
        l1 = l1.next
      }
    }
    if(l1 != null) {
      if(head == null) head = l1
      else tail.next = l1
    }
    else if(l2 != null) {
      if(head == null) head = l2
      else tail.next = l2
    }
    head
  }

  def mergeKLists(lists: Array[ListNode]): ListNode = {
    if (lists == null || lists.isEmpty) null
    else {
      var res: ListNode = null
      var i = 0
      while (i < lists.size) {
        if (res == null) res = lists(i)
        else {
          //merge 2 lists:
          res = mergeTwoLists(res, lists(i))
        }
        i += 1
      }
      res
    }
  }

//  val list1 = new ListNode(1, new ListNode(4, new ListNode(5)))
//  val list2 = new ListNode(1, new ListNode(3, new ListNode(4)))
//  val list3 = new ListNode(2, new ListNode(6))
//  val res = mergeKLists(Array(list1, list2,list3))
//  println(res)
}