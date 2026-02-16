import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> ans = new ArrayList<>();
        ans.add(n);
        
        while (n > 1) {
            if (n % 2 == 0) {
                n = n / 2;                
            } else {    
                n = 3 * n + 1;                              
            }
            ans.add(n);
        }
        return ans.stream().mapToInt(i->i).toArray();
    }
}