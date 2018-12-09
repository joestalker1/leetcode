import java.util.HashMap;

class RandomListNode {
     int label;
     RandomListNode next, random;
     RandomListNode(int x) { this.label = x; }
};

public class CopyListWithRandomPointer {
    private HashMap<RandomListNode, RandomListNode> visited = new HashMap<>();

    private RandomListNode getOrClone(RandomListNode p){
        if(p == null) return null;
        if(!visited.containsKey(p)) {
            RandomListNode newNode = new RandomListNode(p.label);
            visited.put(p, newNode);
            return newNode;
        }
        return visited.get(p);
    }

    public RandomListNode copyRandomList(RandomListNode head) {
        if(head == null) return head;
        RandomListNode newHead = null;
        RandomListNode prev = null;
        for(RandomListNode p = head;p != null; p = p.next) {
           RandomListNode node = getOrClone(p);
           if(newHead == null) newHead = node;
           else prev.next = node;
           node.random = getOrClone(p.random);
           prev = node;
        }
        return newHead;
    }

    public static void main(String ... args) {
        CopyListWithRandomPointer cpm = new CopyListWithRandomPointer();
         RandomListNode n1 = new RandomListNode(1);
         n1.next = new RandomListNode(2);
         n1.next.next = new RandomListNode(2);
         n1.next.next.next = new RandomListNode(2);
         RandomListNode n2 = cpm.copyRandomList(n1);
         System.out.println(n2);
    }
}
