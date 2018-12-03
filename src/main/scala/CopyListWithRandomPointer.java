import java.util.HashMap;

class RandomListNode {
     int label;
     RandomListNode next, random;
     RandomListNode(int x) { this.label = x; }
};

public class CopyListWithRandomPointer {
    public static RandomListNode copyRandomList(RandomListNode head) {
        if(head == null) return head;
        RandomListNode newHead = null;
        RandomListNode prev = null;
        HashMap<RandomListNode,RandomListNode> m = new HashMap<>();
        for(RandomListNode p = head;p != null; p = p.next) {
           RandomListNode node = new RandomListNode(p.label);
           m.put(p, node);
           if(prev != null) prev.next = node;
           else newHead = node;
           prev = node;
        }
        RandomListNode p1 = newHead;
        for(RandomListNode p = head;p != null; p = p.next) {
            p1.random = m.get(p.random);
        }
        return newHead;
    }

    public static
}
