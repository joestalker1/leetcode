import scala.collection.mutable.{ArrayBuffer, ListBuffer}

object ValidateBinarySearchTree extends App {

  class TreeNode(var _value: Int) {
    var value: Int = _value
    var left: TreeNode = null
    var right: TreeNode = null
  }

  def isValidBST(root: TreeNode): Boolean = {
    val nums = new ArrayBuffer[Int]()
    def isValid(node: TreeNode): Boolean = {
      if (node == null) true
      else {
        val left = isValid(node.left)
        val isLess = if(nums.isEmpty) true else nums.last < node.value
        nums += node.value
        val right = isValid(node.right)
        left && isLess && right
      }
    }
    isValid(root)
  }


  val tree = new TreeNode(10)
  tree.left = new TreeNode(5)
  tree.right = new TreeNode(15)
  tree.right.left = new TreeNode(14)
  tree.right.right = new TreeNode(20)
  println(isValidBST(tree))

}

