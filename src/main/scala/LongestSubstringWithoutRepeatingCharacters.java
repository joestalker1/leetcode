package leetcode;

/**
 * Created by jstalker on 10.06.17.
 */
public class LongestSubstringWithoutRepeatingCharacters {
     public int lengthOfLongestSubstring(String s) {
       int len = s.length();
       int i = 0;
       int maxLen = 0;
       while(i < len){
           int j= i;
           int freq[] = new int[256];
           int max = 0;
           while(j < len) {
              char chr = s.charAt(j);
              if(freq[chr] == 0) {
                 max += 1;
                 freq[chr]+=1;
              } else {
                 //max = 0;
                 j = len;
              }
              j+=1;
           }
           if(max > maxLen) maxLen = max;
           i+= 1;
       }
       return maxLen;
     }

    public static void main(String... args) {
         String s1 = "pwwkew";
         LongestSubstringWithoutRepeatingCharacters l = new LongestSubstringWithoutRepeatingCharacters();
         System.out.print(l.lengthOfLongestSubstring(s1));
    }

}
