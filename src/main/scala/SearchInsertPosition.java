package leetcode;

public class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
       //binary search
       int lo = 0;
       int hi = nums.length - 1;
       while(lo <= hi) {
          int mid = lo + (hi - lo)/2;
          if(nums[mid] == target) return mid;
          if(target < nums[mid]) hi = mid - 1;
          else if(target > nums[mid]) lo = mid+1;
       }
       return lo;
    }

    public static void main(String args[]){
        int arr[] = new int[]{1};
        int a = new SearchInsertPosition().searchInsert(arr, 2);
        System.out.println(a);
    }
}
