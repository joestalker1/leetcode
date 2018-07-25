
object ValidateBinarySearchTree extends App {

  class TreeNode(var _value: Int) {
    var value: Int = _value
    var left: TreeNode = null
    var right: TreeNode = null
  }

  def isValidBST(root: TreeNode): Boolean = {
    var hi = Int.MinValue
    def isValid(node: TreeNode): Boolean = {
      if (node == null) true
      else {
        val leftTree = isValid(node.left)
        val leftRes = if (node.left != null) node.left.value < node.value else true
        val rightRes = if (node.right != null) node.right.value > node.value else true
        val inRange = if (hi != Int.MaxValue) node.value > hi else true
        if (leftRes && rightRes && inRange) hi = hi max node.value
        leftRes && rightRes && inRange && leftTree && isValid(node.right)
      }
    }
    isValid(root)
  }
}

//val tree = new TreeNode(2)
//tree.left = new TreeNode(1)
//tree.right = new TreeNode(3)
//println(isValidBST(tree))
