package leetcode;

import java.util.Stack;
import java.lang.Character;

/**
 * Created by jstalker on 25.06.17.
 */
public class ValidParentheses {

    private boolean checkCharInStack(String s,int pos,Character chr, Stack<Character> brackets) {
       return !brackets.empty() && brackets.pop() == chr;
    }

    public boolean isValid(String s) {
       if(s == null) return false;
       int j = 0;
       Stack<Character> brackets = new Stack<Character>();
       while(j < s.length()) {
         if(s.charAt(j) == '(') brackets.push(')');
         else
         if(s.charAt(j) == '[') brackets.push(']');
         else
         if(s.charAt(j) == '{') brackets.push('}');
         else
         if(s.charAt(j) == ')') {
             if(!checkCharInStack(s, j, ')', brackets)) return false;
         }
         else
         if(s.charAt(j) == ']'){
             if(!checkCharInStack(s, j, ']', brackets)) return  false;
         }
         else
         if(s.charAt(j) == '}') {
             if(!checkCharInStack(s, j, '}', brackets)) return  false;
         }
         else return false;
         ++j;
       }
       return brackets.empty();
    }

    public static void main(String ... args) {
        System.out.print(new ValidParentheses().isValid("()"));
    }
}
