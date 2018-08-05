package cracking_code_interview

case class Graph(nodes: Array[Node])
case class Node(name: String, children: Array[Node])

object Task4_1 extends App {
  private def findNode(list:Array[Node], name: String):Option[Node] = {
    graph.nodes.find(_.name == name).getOrElse{
      graph.nodes.
    }
  }

   def route(graph:Graph, from:String, to:String):Boolean = {


   }
}