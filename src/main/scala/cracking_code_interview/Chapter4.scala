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
    var last: TreeNode = null

    def traverse(node: TreeNode): Unit = {
      if (node == null) ()
      else {
        if (x > node.x || x == node.x) {
          traverse(node.right)
        } else if (x < node.x) {
          if (last.x > node.x) last = node
          traverse(node.left)
        }
      }
    }

    last
  }
}

//10,16,28,36,46,70,80,96
object Task4_8 extends App {
  private def descendant(root: TreeNode, x: TreeNode): Boolean = {
    if (root == null || x == null) false
    else {
      if (x.x > root.x) descendant(root.right, x)
      else if (x.x < root.x) descendant(root.left, x)
      else true //equality
    }
  }

  def firstCommonAncestor(root: TreeNode, t1: TreeNode, t2: TreeNode): Option[TreeNode] = {
    if (t1 == null && t2 == null) None
    else if (t1 == null) Some(t2)
    else if (t2 == null) Some(t1)
    else {
      val t1InLeft = descendant(root.left, t1)
      val t2InRight = descendant(root.right, t2)
      if (t1InLeft && t2InRight) return Some(root)
      if (t1InLeft) firstCommonAncestor(root.left, t1, t2)
      else firstCommonAncestor(root.right, t1, t2)
    }
  }
}

// 39, 48, 66, 82
object Task4_9 extends App {
  private def traverse(node: TreeNode): List[List[Int]] = {
    if (node != null && node.left == null && node.right == null) {
      List(List(node.x))
    } else {
      var leftList = traverse(node.left)
      var rightList = traverse(node.right)
      leftList = leftList.map(node.x :: _)
      rightList = rightList.map(node.x :: _)
      for {list1 <- leftList
           list2 <- rightList
      } yield (list1 ++ list2)
    }
  }

  def bstSequence(node: TreeNode): List[List[Int]] = {
    if (node == null) List.empty
    else traverse(node)
  }
}

//4,11,18,31,37
object Task4_10 extends App {
  private val nullNode = "null"

  private def prefix(root: TreeNode, traversed: String = ""): String = {
    if (root == null) traversed + s" $nullNode"
    else {
      val newTraversed = traversed + s" ${root.x} "
      prefix(root.left, newTraversed) + prefix(root.right, newTraversed)
    }
  }

  private def checkSubtree(root:TreeNode, matched: String):Boolean = {
     val path = prefix(root)
     if(path == matched) true
     else checkSubtree(root.left, matched) || checkSubtree(root.right, matched)
  }

  def checkSubtree(t1: TreeNode, t2: TreeNode): Boolean = {
     val matched = prefix(t2)
     checkSubtree(t1, matched)
  }
}

//#42, 54, 62, 75, 89, 99, 112, 119
object Task4_11 extends App {
   private def traverse(node:TreeNode,list:List[Int]):List[Int] = {
      if(node == null) list
      else {
        val list1 = traverse(node.left, list)
        val list2 = traverse(node.right, list)
        (list1 :+ node.x) ++ list2
      }
   }

   def randomNode(node:TreeNode, n:Int): Int = {
      val list = traverse(node, List.empty)
      list(n)
   }
}
// 6,14,52,68,77,87,94,103,108,115
object Task4_12 extends App {
  private def traverse(node:TreeNode,list:List[Int]):List[Int] = {
    if(node == null) list
    else {
      val list1 = traverse(node.left, list)
      val list2 = traverse(node.right, list)
      (list1 :+ node.x) ++ list2
    }
  }

  def pathWithSum(root:TreeNode, sum: Int):Int = {
    if(root == null) 0
    else {
       val arr = traverse(root, List.empty).toArray
       var sumIndex = Set.empty[Int]
       var total = 0
       var ways = 0
       for(i <- 0 until arr.length){
         total += arr(i)
         if(total == sum) ways += 1
         val rest = total - sum
         if(sumIndex(rest)) ways+=1
         sumIndex = sumIndex + total
       }
       ways
    }
  }
}