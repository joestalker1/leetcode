package leetcode;

/**
  * Created by jstalker on 09.07.17.
  */
class RemoveElements {
  int removeElement(int [] nums, int val) {
    if(nums.length == 0) return nums.length;
      int shift = 0;
      for(int i =0;i< nums.length; ++i){
        if(nums[i] == val) shift++;
        else if(i > 0){
          for(int j=1;j<=shift;++j){
            nums[i-j] = nums[i];
          }
        }
      }
      return nums.length - shift;
  }
}
