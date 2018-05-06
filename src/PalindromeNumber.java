package leetcode;

/**
 * Created by jstalker on 18.06.17.
 */
public class PalindromeNumber {
    public static boolean isPalindrome(int x) {
      if(x == 0) return true;
      if(x < 0) return false;
      int i = 0,j = 9;
      int k = 1000000000;
      while(x / k == 0) {
          k /= 10;
          j-= 1;
      }
      while(i <= j) {
        int l = getDigit(x, j);
        int r = getDigit(x, i);
        if(l != r) return false;
        j-= 1;
        i += 1;
      }
      return true;
    }
    //from right ot left based on 0.
    private static int getDigit(int num,int pos){
       while(pos > 0){
          num /= 10;
          pos -= 1;
       }
       return num % 10;
    }

    public static void main(String... args) {
       System.out.println(isPalindrome(10));
       System.out.println(isPalindrome(-101));
       System.out.println(isPalindrome(10001));
       System.out.println(isPalindrome(121));
       System.out.println(isPalindrome(1000021));
    }
}
