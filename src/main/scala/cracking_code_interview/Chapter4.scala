package cracking_code_interview


object Task4_1 extends App {

  case class Graph(nodes: Array[Node])

  case class Node(name: String, children: Array[Node])

  private var name2Node = Map.empty[String, Node]

  def register(node: Node): Unit = {
    name2Node = name2Node + (node.name -> node)
    node.children.foreach { n =>
      name2Node = name2Node + (n.name -> n)
    }
  }

  private def visit(node: Node, to: String): Boolean = {
    node.name == to || node.children.find(_.name == to).nonEmpty
  }

  def route(graph: Graph, from: String, to: String): Boolean = {
    val fromNode = name2Node(from)
    var queue = scala.collection.immutable.Queue[Node]()
    queue = queue.enqueue(fromNode)
    var found = false
    while (queue.nonEmpty && !found) {
      val (n, q) = queue.dequeue
      queue = q
      found = visit(n, to)
      n.children.foreach { a =>
        queue = queue.enqueue(a)
      }
    }
    found
  }
}

object Task4_2 extends App {

  import Trees._

  private def minSearchTree(arr: Array[Int], from: Int, to: Int): TreeNode = {
    if (from > to) null
    else if (from == to) TreeNode(arr(from))
    else {
      val mid = from + (to - from) / 2
      TreeNode(arr(mid), minSearchTree(arr, from, mid - 1), minSearchTree(arr, mid + 1, to))
    }
  }

  def minimalSearchTree(arr: Array[Int]): TreeNode = {
    if (arr.isEmpty) null
    else minSearchTree(arr, 0, arr.length - 1)
  }
}

object Task4_3 extends App {

  import Trees._

  private def traverse(node: TreeNode, level: Int, levelToList: scala.collection.mutable.Map[Int, List[Int]]): Unit = {
    if (node == null) ()
    else {
      var list = levelToList.getOrElse(level, Nil)
      list = node.x :: list
      levelToList += (level -> list)
      traverse(node.left, level + 1, levelToList)
      traverse(node.right, level + 1, levelToList)
    }
  }

  def listDepth(tree: TreeNode): List[List[Int]] = {
    if (tree == null) Nil
    else {
      val levelToList = scala.collection.mutable.Map[Int, List[Int]]()
      traverse(tree, 0, levelToList)
      levelToList.map(_._2)(scala.collection.breakOut)
    }
  }
}

//21,33,49,105,124
object Task4_4 extends App {

  import Trees._

  def checkBalanced(root: TreeNode): Boolean = {
    var balanced = true

    def checkHeight(tree: TreeNode): Int = {
      if (tree == null) 0
      else {
        val leftHeight = checkHeight(tree.left)
        val rightHeight = checkHeight(tree.right)
        if (Math.abs(leftHeight - rightHeight) > 1) balanced = false
        1 + (leftHeight max rightHeight)
      }
    }

    checkHeight(root)
    balanced
  }
}

object Trees {

  case class TreeNode(x: Int, left: TreeNode = null, right: TreeNode = null)

}

//#35,57,86,113,128
object Task4_5 extends App {

  import Trees._

  def validateTree(root: TreeNode): Boolean = {
    def traverse(node: TreeNode, min: Int, max: Int): Boolean = {
      if (node == null) true
      else {
        if (node.x < min || node.x > max) false
        else traverse(node.left, min, node.x) && traverse(node.right, node.x, max)
      }
    }

    traverse(root, Int.MinValue, Int.MaxValue)
  }

}

//79, 91
import Trees._

object Task4_6 extends App {
  def succ(x: Int): TreeNode = {
    var last:TreeNode = null
    def traverse(node: TreeNode): Unit = {
      if (node == null) ()
      else {
        if (x  > node.x || x == node.x) {
          traverse(node.right)
        } else if(x < node.x) {
          if(last.x > node.x) last = node
          traverse(node.left)
        }
      }
    }
    last
  }
}
//26, 47, 60, 85, 125, 133
object Task4_7 extends App {

}