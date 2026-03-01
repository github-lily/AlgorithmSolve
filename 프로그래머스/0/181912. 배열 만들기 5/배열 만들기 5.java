import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        
        List<Integer> ans = new ArrayList<>();
        
        for (String intStr : intStrs) {
            int temp = Integer.parseInt(intStr.substring(s,s+l));
            
            if (temp>k) {
                ans.add(temp);
            }
        }
        
        return ans.stream().mapToInt(i->i).toArray();
        
    }
}