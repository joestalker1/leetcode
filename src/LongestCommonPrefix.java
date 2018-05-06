package leetcode;

/**
 * Created by jstalker on 24.06.17.
 */
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
       if(strs == null || strs.length == 0) return "";
       int index = findMinLen(strs);
       String prefix = "";
       int low = 0;
       int high = index;
       while(low <= high){
           int mid = low + (high - low) / 2;
           if(allCommonPrefix(strs, strs[0], low, mid)){
               prefix = prefix + strs[0].substring(low, mid + 1);
               low = mid + 1;
           } else high = mid - 1;
       }
       return prefix;
    }

    private int findMinLen(String strs[]){
       int len = strs[0].length();
       for(int i = 1;i < strs.length; ++i){
           if(len > strs[i].length()) len = strs[i].length();
       }
       return len;
    }

    private Boolean allCommonPrefix(String strs[], String s,int start, int end) {
        for(int i = 0;i < strs.length; ++i) {
           for(int j = start; j <= end;++j) {
               if(j >= s.length() || j >= strs[i].length() || strs[i].length() == 0 || s.length() == 0 || strs[i].charAt(j) != s.charAt(j)) return false;
           }
        }
        return true;
    }

    public static void main(String... args) {
       String arr [] = {"geeksforgeeks", "geeks", "geek","geezer"};
       String arr2 [] = {"abc","abcc","abc","abca","abca"};
       String lcp = new LongestCommonPrefix().longestCommonPrefix(arr2);
       System.out.println(lcp);
    }
}
