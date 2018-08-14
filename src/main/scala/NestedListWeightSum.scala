//object NestedListWeightSum extends App {
//  private def dfs(ni: NestedInteger, level: Int): Int = {
//    var sum = 0
//    if (ni.isInteger) sum += level * ni.getInteger
//    if(ni.getList!= null) sum += dfs(ni.getList, level + 1)
//    sum
//  }
//
//  private def dfs(nestedList: List[NestedInteger], level: Int): Int = {
//    var sum = 0
//    for (ni <- nestedList) {
//      sum += dfs(ni, level+ 1)
//    }
//    sum
//  }
//
//  def depthSum(nestedList: List[NestedInteger]): Int = {
//    if (nestedList == null || nestedList.isEmpty) 0
//    else dfs(nestedList,1)
//  }
//
//}

