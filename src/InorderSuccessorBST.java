class Solution {
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    private TreeNode traverse(TreeNode node, TreeNode succ, int a){
        if(node == null) return succ;
        if(node.val > a && (succ == null || succ.val > node.val))  succ = node;
        TreeNode left = traverse(node.left, succ, a);
        TreeNode right = traverse(node.right, succ, a);
        if(left != null && right == null) return left;
        if(left == null && right != null) return right;
        if(left.val < right.val) return left;
        return right;
    }

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if(root == null) return null;
        return traverse(root, null, p.val);
    }
}