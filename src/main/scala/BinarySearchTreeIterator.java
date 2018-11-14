import java.util.List;
import java.util.LinkedList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class BSTIterator {
    private List<TreeNode> stack = new LinkedList<>();

    public BSTIterator(TreeNode root) {
        pushAll(root);
    }

    /**
     * @return whether we have a next smallest number
     */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    public int next() {
        TreeNode tmpNode = stack.remove(stack.size()-1);
        pushAll(tmpNode.right);
        return tmpNode.val;
    }

    private void pushAll(TreeNode node) {
        for (; node != null; stack.add(node), node = node.left);
    }
}

public class BinarySearchTreeIterator {
    public static void main(String... args) {
        TreeNode root = new TreeNode(5);
        root.right = new TreeNode(6);
        root.left = new TreeNode(3);
        root.left.left = new TreeNode(2);
        root.left.left.left = new TreeNode(1);
        root.left.right = new TreeNode(4);

        BSTIterator iterator = new BSTIterator(root);
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
//
//
//        root = new TreeNode(3);
//        root.right = new TreeNode(4);
//        root.left = new TreeNode(2);
//        root.left.left = new TreeNode(1);
//        iterator = new BSTIterator(root);
//        while (iterator.hasNext()) {
//            System.out.println(iterator.next());
//        }
//
//        root = new TreeNode(3);
//        root.right = new TreeNode(4);
//        root.left = new TreeNode(1);
//        root.left.right = new TreeNode(2);
//        iterator = new BSTIterator(root);
//        while (iterator.hasNext()) {
//            System.out.println(iterator.next());
//        }
//
//        root = new TreeNode(2);
//        root.right = null;
//        root.left = new TreeNode(1);
//        iterator = new BSTIterator(root);
//        while (iterator.hasNext()) {
//            System.out.println(iterator.next());
//        }
//        root = new TreeNode(1);
//        root.left = null;
//        root.right = new TreeNode(2);
//        iterator = new BSTIterator(root);
//        while (iterator.hasNext()) {
//            System.out.println(iterator.next());
//        }

    }
}