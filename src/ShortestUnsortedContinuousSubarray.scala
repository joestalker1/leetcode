package leetcode




object ShortestUnsortedContinuousSubarray extends App {
  case class Node(k: Int,i: Int, var left: Option[Node] = None, var right: Option[Node] = None)

  private def insert(from: Node, a: Int, i: Int)(ifLess: Int => Unit): Unit = {
    if(from.k > a) {
      if(from.k > a) ifLess(from.i)
      from.left.map(left => insert(left, a, i)(ifLess)).getOrElse {
        from.left = Some(Node(a, i))
      }
    } else {
      from.right.map(right => insert(right, a, i)(ifLess)).getOrElse {
        from.right = Some(Node(a, i))
      }
    }

  }

  def findUnsortedSubarray(nums: Array[Int]): Int = {
    if (nums.isEmpty || nums.size == 1) 0
    else {
      var start:Option[Int] = None
      var end:Option[Int] =  None
      val root = Node(nums(0), 0)
      for(i <- 1 until nums.size){
         insert(root, nums(i), i){ ind =>
           if(start.isEmpty) start = Some(ind)
           else start.filter(_ > ind).foreach(_ => start = Some(ind))
           end = Some(i) //most right index
         }
      }
      (for {
        s <- start
        e <- end
      } yield (e - s + 1)).fold(0)(identity[Int])
    }
  }

  val arr1 = Array(2, 1) //2
  assert(findUnsortedSubarray(arr1) == 2)

  val arr2 = Array(2,3,3,2,4) //3
  assert(findUnsortedSubarray(arr2) == 3)

  val arr3 = Array(1, 2, 3, 3, 3) //0
  assert(findUnsortedSubarray(arr3) == 0)

  val arr4 = Array(1, 3, 2, 2, 2) //4
  assert(findUnsortedSubarray(arr4) == 4)

  val arr5 = Array(2,6,4,8,10,9,15) //5
  assert(findUnsortedSubarray(arr5) == 5)

  val arr6 = Array(1,3,5,4,2) //4
  assert(findUnsortedSubarray(arr6) == 4)

}
