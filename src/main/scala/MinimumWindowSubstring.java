
public class MinimumWindowSubstring {
    public static String minWindow(String s, String t) {
         if(s == null || t == null || s.length() < t.length()) return "";
         int map[] = new int[128];
         for(int i = 0; i< t.length(); i++){
             map[t.charAt(i)] += 1;
         }
         int counter = t.length();
         int begin = 0,end = 0;
         int d = Integer.MAX_VALUE;
         int head = 0;
         while(end < s.length()){
             if(map[s.charAt(end)] > 0) counter -=1;
             map[s.charAt(end)] -= 1;
             end += 1;
             while(counter == 0){
                 if(end - begin < d) {
                     d = end - begin;
                     head = begin;
                 }
                 if(map[s.charAt(begin)] == 0) counter += 1;
                 map[s.charAt(begin)] += 1;
                 begin += 1;

             }
         }
         return d == Integer.MAX_VALUE ? "": s.substring(head, head + d);
    }

    public static void main(String ... args){
        System.out.println(minWindow("ADOBECODEBANC", "ABC"));
    }
}
