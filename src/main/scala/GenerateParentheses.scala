import scala.collection.mutable.ListBuffer

object GenerateParentheses extends App {
  private def generate(s: Array[Char], pos:Int,n: Int,open:Int,close:Int, res:ListBuffer[String]):Unit = {
     if(close == n) {
       res += s.mkString("")
     }
     else {
        if(open > close){
          s(pos) = ')'
          generate(s, pos + 1, n, open, close + 1, res)
        }
        if(open < n){
           s(pos) = '('
           generate(s, pos + 1, n, open + 1, close, res)
        }
     }
  }

  def generateParenthesis(n: Int): List[String] = {
     val res = new ListBuffer[String]()
     generate(Array.ofDim[Char](2* n),0, n, 0, 0,res)
     res.toList
  }

  generateParenthesis(3)
}
