import java.util.List;

interface NestedInteger {
    public boolean isInteger();

    public Integer getInteger();

    public void setInteger(int value);


    public void add(NestedInteger ni);

    public List<NestedInteger> getList();
}

class NestedListWeightSum2 {
    private int dfs(List<NestedInteger> nestedList, int level) {
        int sum = 0;
        for (NestedInteger ni : nestedList) {
            if(ni.isInteger()) sum += level * ni.getInteger();
            if(ni.getList()!= null) sum += dfs(ni.getList(), level + 1);
        }
        return sum;
    }

    public int depthSum(List<NestedInteger> nestedList) {
        if (nestedList == null || nestedList.size() == 0)
            return 0;
        return dfs(nestedList, 1);
    }
}