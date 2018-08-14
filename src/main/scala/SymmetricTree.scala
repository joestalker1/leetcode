class TreeNode(var _value: Int) {
  var value: Int = _value
  var left: TreeNode = null
  var right: TreeNode = null
}

object SymmetricTree extends App {
  private def isMirror(x: TreeNode, y:TreeNode):Boolean = {
    if(y == null && x == null) true
    else if(x == null || y == null) false
    else if(x.value != y.value) false
    else isMirror(x.left, y.right) && isMirror(x.right, y.left)
  }

  def isSymmetric(root: TreeNode): Boolean = {
       if(root == null) true
       else isMirror(root, root)
  }
}
