case class AvlNode(key: Int, var height: Int = 0, var children: Int = 0, var left: AvlNode = null, var right: AvlNode = null)

object AvlTree {

  implicit class EnrichedAvlTree(val node: AvlNode) extends AnyVal {
    def h: Int = if (node == null) 0 else node.height

    def left(n: AvlNode): AvlNode = {
      if (node.left == null) {
        if (n != null) node.children += 1
      } else {
        if (n == null) node.children -= 1
      }
      node.left = n
      node
    }

    def right(n: AvlNode): AvlNode = {
      if (node.right == null) {
        if (n != null) node.children += 1
      } else {
        if (n == null) node.children -= 1
      }
      node.right = n
      node
    }
  }

}

import AvlTree._

class AvlTree(var root: AvlNode = null) {
  def rightRotate(y: AvlNode): AvlNode = {
    val x = y.left
    val t2 = x.right
    x.right(y)
    y.left(t2)
    y.height = (y.left.h max y.right.h) + 1
    x.height = (x.left.h max x.right.h) + 1
    x
  }


  private def balance(n: AvlNode): Int = {
    if (n == null) 0
    else n.left.h - n.right.h
  }

  def leftRotate(x: AvlNode): AvlNode = {
    val y = x.right
    val t2 = y.left
    y.left(x)
    x.right(t2)
    x.right.height = (x.left.h max x.right.h) + 1
    y.height = (y.left.h + y.right.h) + 1
    y
  }

  def insert(key: Int): AvlNode = {
    val node = insert(root, key)
    if (root == null) root = node
    node
  }

  private def insert(node: AvlNode, key: Int): AvlNode = {
    if (node == null) return AvlNode(key, 0)
    else if (key < node.key) node.left(insert(node.left, key))
    else if (key >= node.key) node.right(insert(node.right, key))

    node.height = 1 + (node.left.h max node.right.h)

    val bal = balance(node)

    if (bal > 1 && key < node.left.key) return rightRotate(node)

    // Right Right Case
    if (bal < -1 && key > node.right.key) return leftRotate(node)

    // Left Right Case
    if (bal > 1 && key > node.left.key) {
      node.left(leftRotate(node.left))
      return rightRotate(node)
    }

    // Right Left Case
    if (bal < -1 && key < node.right.key) {
      node.right(rightRotate(node.right))
      return leftRotate(node)
    }
    /* return the (unchanged) node pointer */
    node
  }
}