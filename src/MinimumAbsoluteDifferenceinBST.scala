package leetcode

case class TreeNode(var _value: Int) {
  var value: Int = _value
  var left: TreeNode = null
  var right: TreeNode = null
}

object MinimumAbsoluteDifferenceinBST extends App {
  def getMinimumDifference(root: TreeNode): Int = {
     next(root, Int.MaxValue)
  }

  private def next(root: TreeNode, minDiff: Int):Int = {
    if(root == null) minDiff
    else {
      val a = root._value
      val diffWithA = getMinimumDifferenceWith(root.left, a, minDiff) min getMinimumDifferenceWith(root.right,a, minDiff)
      next(root.left, diffWithA) min next(root.right, diffWithA)
    }
  }

  private def getMinimumDifferenceWith(root: TreeNode, a: Int, minDiff: Int): Int = {
     if(root == null) minDiff
     else {
       val diff = Math.abs(a - root._value) min minDiff
       getMinimumDifferenceWith(root.right, a, diff) min getMinimumDifferenceWith(root.left, a, diff)
     }
  }

  val root = TreeNode(1)
  root.right = TreeNode(3)
  root.right.left = TreeNode(2)

  println(getMinimumDifference(root))
}

