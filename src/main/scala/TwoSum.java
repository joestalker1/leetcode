package leetcode;

import java.util.*;

/**
 * Created by jstalker on 15.01.17.
 */
public class TwoSum {

    public static void main(String ... args){
        int nums[] = {3,2,4};
        int target = 6;
        int indices[] = new TwoSum().twoSum(nums, target);
        System.out.println(indices[0]+":"+indices[1]) ;
    }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer,List<Integer>> num2pos = new HashMap<>();
        for(int i = 0;i < nums.length;i++) {
            List<Integer> list = num2pos.get(nums[i]);
            if(list ==null) list = new ArrayList<>();
            list.add(i);
            num2pos.put(nums[i], list);
        }
        Arrays.sort(nums);
        int i = 0;
        int j = nums.length -1;
        int indices[] = new int[2];
        while(i < nums.length){
          while(i != j && nums[i] + nums[j] > target && j > 0) j-=1;
          if(j >= 0 && i != j && nums[i]+nums[j] == target){
              indices[0] = findPos(nums[i],num2pos);
              indices[1] = findPos(nums[j],num2pos);
              if(indices[0] > indices[1]) {
                  int a = indices[0];
                  indices[0] = indices[1];
                  indices[1] = a;
              }
              break;
          }
          i+=1;
        }
        return indices;
    }

    private int findPos(int num,Map<Integer,List<Integer>> num2pos){
        List<Integer> list = num2pos.get(num);
        int pos = list.get(0);
        list.remove(0);
        return pos;
    }
}