import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.LinkedList;

class TreeNode1 {
     int val;
     TreeNode1 left;
     TreeNode1 right;
     TreeNode1(int x) { val = x; }
 }


public class SerializeDeserializeBST {
     public static void main(String[] args) {
         TreeNode1 left = new TreeNode1(2);
         left.left = new TreeNode1(22);
         left.right = new TreeNode1(23);
         TreeNode1 right = new TreeNode1(3);
         right.left = new TreeNode1(32);
         right.right = new TreeNode1(33);
         TreeNode1 root = new TreeNode1(1);
         root.left = left;
         root.right = right;
         Codec codec = new Codec();
         String s = codec.serialize(root);
         System.out.println(s);
         TreeNode1 node = codec.deserialize(s);
         String s1 = codec.serialize(node);
         System.out.println(s.equals(s1));
     }
}

class Codec {
    private static String NULL_STR = "n";

    private void serialize(TreeNode1 root, ArrayList<Integer> buffer){
        if(root == null) {
            buffer.add(null);
            return;
        }
        buffer.add(root.val);
        serialize(root.left, buffer);
        serialize(root.right, buffer);
    }

    private String asString(Integer x){
        if(x == null) return NULL_STR;
        return x.toString();
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode1 root) {
       ArrayList<Integer> buffer = new ArrayList<>();
       serialize(root, buffer);
       return buffer.stream().map(this::asString).collect(Collectors.joining(","));
    }

    public TreeNode1 deserialize(String data) {
        String[] strings = data.split(",");
        if(strings == null || strings.length == 0) return null;
        LinkedList<String> list = new LinkedList<>();
        for(String str: strings){
             list.add(str);
        }
        return deserialize(list);
    }

    private TreeNode1 deserialize(LinkedList<String> strings){
        if(strings.size() == 0) return null;
        if(strings.get(0).equals(NULL_STR)) {
            strings.removeFirst();
            return null;
        }
        int a = Integer.valueOf(strings.get(0));
        TreeNode1 node = new TreeNode1(a);
        strings.removeFirst();
        node.left = deserialize(strings);
        node.right = deserialize(strings);
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));