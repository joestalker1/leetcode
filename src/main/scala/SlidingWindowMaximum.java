public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums == null || k == 0) return new int[0];
        int [] res = new int[nums.length - k + 1];
        java.util.PriorityQueue<Integer> queue = new java.util.PriorityQueue<>(new java.util.Comparator<Integer>(){
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });
        for(int i = 0;i < k;i++){
            queue.add(nums[i]);
        }
        res[0] = queue.peek();
        for(int i = k;i< nums.length;i++){
            queue.add(nums[i]);
            queue.remove(nums[i - k]);
            res[i - k + 1] = queue.peek();
        }
        return res;
    }
}
