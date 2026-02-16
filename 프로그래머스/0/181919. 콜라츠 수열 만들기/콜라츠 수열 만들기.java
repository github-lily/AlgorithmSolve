import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> ans = new ArrayList<>();
        ans.add(n);
        
        while (n > 0) {
            // 짝수
            if (n % 2 == 0) {
                n = n / 2;                
            // 홀수
            } else {    
                n = 3 * n + 1;                              
            }
            ans.add(n);
            if (n==1) {
                break;
            }
        }
        return ans.stream().mapToInt(i->i).toArray();
    }
}