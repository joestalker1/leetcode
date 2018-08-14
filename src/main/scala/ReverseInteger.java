package leetcode;

/**
 * Created by jstalker on 18.06.17.
 */
public class ReverseInteger {
    public static int reverse(int x) {
      long res = 0;
      int a = Math.abs(x);
      while(a > 0){
        int digit = a % 10;
        //shift res to the right
        res = res* 10 + digit;
        if(res > Integer.MAX_VALUE) return 0;
        a = a / 10;
      }
      if(x < 0) return (int)-res;
      return (int)res;
    }

    public static void main(String... args) {
         System.out.println(reverse(1534236469)) ;
    }

}
