class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
from collections import defaultdict

class Solution:
    def depthSumInverse(self, nestedList):
        if not nestedList:
            return 0

        m = defaultdict(list)
        def traverse(nl, level):
            for n in nl:
                if n.isInteger():
                   m[level].append(n.getInteger())
                else:
                   traverse(n.getList(), level + 1)
        traverse(nestedList, 1)
        if len(m.keys()) > 0:
            max_level = max(m.keys())
        else:
            max_level = 0
        list_sum = 0
        for k in m.keys():
            w = max_level - k + 1
            list_sum += (sum(m[k]) * w)
        return list_sum

