import java.util.*;

class Solution {
    public String solution(String my_string, int[] indices) {
        StringBuilder ans = new StringBuilder(my_string);
        Arrays.sort(indices);

        for (int i = indices.length-1; i >= 0; i--) {
            ans.deleteCharAt(indices[i]);
        }
        
        return ans.toString();
    }
}