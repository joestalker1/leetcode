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
        int carry = 0;
        ListNode last = null;
        ListNode first = null;
        while (l1 != null && l2 != null) {
            int sum = l1.val + l2.val + carry;
            int digit = sum % 10;
            if (sum >= 10) carry = 1;
            else carry = 0;
            l1 = l1.next;
            l2 = l2.next;
            ListNode newNode = new ListNode(digit);
            if (first == null) last = first = newNode;
            else {
                last.next = newNode;
                last = newNode;
            }
        }

        if (l1 != null) last.next = l1;
        else if (l2 != null) last.next = l2;

        ListNode next = last.next;
        while (next != null && carry > 0) {
            int res = next.val + carry;
            next.val = res % 10;
            if (res >= 10) carry = 1;
            else carry = 0;
            next = next.next;
            if (next != null) last = next;
        }
        if (carry > 0) {
            while(last.next != null) last = last.next;
            last.next = new ListNode(carry);
        }
        return first;
    }

}

