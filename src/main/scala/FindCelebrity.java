import java.util.Set;
import java.util.HashSet;

class Relation {
    boolean knows(int a, int b) {
        if(a == 1) return true;
        return false;
    }
}

public class FindCelebrity extends Relation {
    public int findCelebrity(int n) {
        int canditate = 0;
        for(int i = 1; i< n;i++){
            if(knows(canditate,i)){
                canditate = i;
            }
        }
        for(int i = 0; i< n;i++){
            if((i!=canditate) &&(knows(canditate,i) || !knows(i, canditate))) return -1;
        }
        return canditate;
    }

    public static void main(String ... args){
        FindCelebrity fc = new FindCelebrity();
        System.out.println(fc.findCelebrity(2));
    }
}
