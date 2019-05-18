import java.util.*;

public class MaximumFrequencyStack {
    private Map<Integer,Integer> freq = new HashMap<>();
    private Map<Integer, Stack<Integer>> group = new HashMap<>();
    private int maxFreq;

    public void push(int x) {
        int f = freq.getOrDefault(x, 0);
        f += 1;
        freq.put(x, f);
        if(f > maxFreq)
            maxFreq = f;
        group.computeIfAbsent(f, z -> new Stack()).push(x);
    }


    public int pop() {
        Stack<Integer> stack = group.get(maxFreq);
        int max = stack.pop();
        freq.put(max, freq.get(max) - 1);
        if(stack.isEmpty()){
            group.remove(maxFreq);
            maxFreq -= 1;
        }
        return max;
    }


    public static void main(String ... args){
        MaximumFrequencyStack stack = new MaximumFrequencyStack();
        //[5,7,5,7,4,5]
        stack.push(5);
        stack.push(7);
        stack.push(5);
        stack.push(7);
        stack.push(4);
        stack.push(5);
        for(int i = 0; i< 6;i++){
            System.out.println(stack.pop());
        }
    }

}
