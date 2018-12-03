import Trie._

class Trie() {
  /** Initialize your data structure here. */
  private val root = TrieNode()
  private var levelToTrieNode = Map.empty[Int, List[TrieNode]]

  /** Inserts a word into the trie. */
  def insert(word: String) {
    var crawl = root
    for (level <- 0 until word.length) {
      val index = word(level)
      if (crawl.children(index) == null) {
        crawl.children(index) = TrieNode(parent = crawl)
        val list = levelToTrieNode.getOrElse(level, List.empty)
        levelToTrieNode = levelToTrieNode + (level -> (crawl.children(index) :: list))
      }
      crawl = crawl.children(index)
    }
    crawl.isEndOfWord = true
  }

  /** Returns if the word is in the trie. */
  def search(word: String): Boolean = {
    val (len, node) = find(word)
    node.isEndOfWord && len == word.length
  }

  private def find(word:String): (Int, TrieNode) = {
    var node = root
    var i = 0
    while(i < word.length && node.children(word(i)) != null) {
      val ch = word(i)
      node = node.children(ch)
      i += 1
    }
    (i , node)
  }


  /** Returns if there is any word in the trie that starts with the given prefix. */
  def startsWith(prefix: String): Boolean = {
     val (len, _) = find(prefix)
     len == prefix.length
  }
}

object Trie {
  val alphabetSize = 127

  // I don't want to deal with immutable IndexedSeq.
  case class TrieNode(var children: Array[TrieNode] = Array.ofDim[TrieNode](alphabetSize), var isEndOfWord: Boolean = false, parent:TrieNode = null)
}


object PrefixTree extends App {
  val trie = new Trie()
  trie.insert("apple")
  println(trie.search("appl"))
  println(trie.startsWith("app"))
}
