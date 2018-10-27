package leetcode


class ListNode1(var _x: Int = 0) {
     var next: ListNode1 = null
     var x: Int = _x
}


trait MergeLists {
  val m = Map.empty[String, String]

  def mergeTwoLists(l1: ListNode1, l2: ListNode1): ListNode1 = {
     if(l1 == null && l2 == null) null
     else if(l1 != null && l2 == null) l1
     else if(l2 != null && l1 == null) l2
     else {
       if(l1.x < l2.x) {
         l1.next = mergeTwoLists(l1.next, l2)
         l1
       } else {
         l2.next = mergeTwoLists(l1, l2.next)
         l2
       }
     }
  }
}
