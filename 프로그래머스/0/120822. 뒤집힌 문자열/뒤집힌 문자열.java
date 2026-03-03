import java.util.*;

class Solution {
    public String solution(String my_string) {
        StringBuilder ans = new StringBuilder();
        
        for (int i = my_string.length()-1; 0 < i+1 ; i--) {
            ans.append(my_string.charAt(i));
        }
        
        return ans.toString();
        
    }
}