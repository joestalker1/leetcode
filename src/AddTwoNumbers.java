package leetcode;


import java.util.List;

class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
     }
}

 public class AddTwoNumbers {
     public static void main(String... args) {
         ListNode l1 = new ListNode(1);
         //l1.next = new ListNode(8);
         //l1.next.next = new ListNode(3);
         ListNode l2 = new ListNode(9);
         l2.next = new ListNode(9);
         //l2.next.next = new ListNode(4);
         ListNode res = addTwoNumbers(l1, l2);
         ListNode r = res;
         //System.out.println(indices[0]+":"+indices[1]) ;
     }


     public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
         int overflow = 0;
         ListNode last = null;
         ListNode first = null;
         while(l1 != null && l2 != null){
             int sum = l1.val + l2.val;
             sum += overflow;
             int diff = sum - 10;
             if(diff > 0 || sum == 10) {
                 overflow = 1;
                 sum = diff;
             }
             else overflow = 0;
             l1 = l1.next;
             l2 = l2.next;
             ListNode newNode = new ListNode(sum);
             if(first == null)
                 last = first = newNode;
             else {
                 last.next = newNode;
                 last = newNode;
             }

         }

         if(l1 != null) {
             last.next = sumWithShifting(l1, overflow);
         }
         if(l2 != null) {
             last.next = sumWithShifting(l2, overflow);
         }
         if(overflow > 0 && l1 == null && l2 == null) {
              last.next = new ListNode(overflow);
              last = last.next;

         }
         return first;
     }


     private static ListNode sumWithShifting(ListNode l,int add) {
         ListNode last = l;
         ListNode first = l;
         while(l != null || add > 0){
           if(add > 0 && l != null){
               int sum = l.val + add;
               if(sum >= 10) {
                   l.val = sum - 10;
                   if(l.next == null) {
                      last = l.next = new ListNode(0);
                   }
                   add = 1;
               } else {
                   l.val = sum;
                   add = 0;
               }
           } else if(add > 0 && l == null){
               last = l.next = new ListNode(add);
               add = 0;
           } else if(add == 0 && l!= null){
               if(l.next != null) last = l.next;
           }
           l = l.next;
         }
         return first;
     }
 }
