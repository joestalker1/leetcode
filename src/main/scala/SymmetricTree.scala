class TreeNode_(var _value: Int) {
  var value: Int = _value
  var left: TreeNode_ = null
  var right: TreeNode_ = null
}

object SymmetricTree extends App {
  private def isMirror(x: TreeNode_, y:TreeNode_):Boolean = {
    if(y == null && x == null) true
    else if(x == null || y == null) false
    else if(x.value != y.value) false
    else isMirror(x.left, y.right) && isMirror(x.right, y.left)
  }

  def isSymmetric(root: TreeNode_): Boolean = {
       if(root == null) true
       else isMirror(root, root)
  }
}
