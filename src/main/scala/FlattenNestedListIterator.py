class NestedInteger(object):
    def isInteger(self):
        return

    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    def getInteger(self):
        return

    #        """
    #        @return the single integer that this NestedInteger holds, if it holds a single integer
    #        Return None if this NestedInteger holds a nested list
    #        :rtype int
    #        """

    def getList(self):
        return


#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class IntVal(NestedInteger):
    def __init__(self, a):
        self.a = a

    def isInteger(self):
        return True

    def getInteger(self):
        return self.a

    def getList(self):
        return None


class ListList(NestedInteger):
    def __init__(self, listvals):
        self.listvals = listvals

    def isInteger(self):
        return False

    def getInteger(self):
        return None

    def getList(self):
        return self.listvals


# iterators
class NestedIterator:
    def __init__(self, lst):
        self.q = []
        self.flatten(lst)

    def flatten(self, lst):
        for ni in lst:
            if ni.isInteger():
                self.q.append(ni.getInteger())
            else:
                self.flatten(ni.getList())

    def next(self):
        a = self.q[0]
        self.q.pop(0)
        return a

    def hasNext(self):
        return len(self.q)



# [[1,2],3,[4,5]]
intlist1 = ListList([IntVal(1), IntVal(2)])
intlist2 = ListList([IntVal(4), IntVal(5)])
ne = NestedIterator([ListList([])])
while ne.hasNext():
    print(ne.next())
