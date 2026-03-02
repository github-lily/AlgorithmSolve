import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> ans = new ArrayList<>();

        for (int i = 0; i < my_string.length(); i++) {
            ans.add(my_string.substring(i));
        }

        Collections.sort(ans);
        
        return ans.toArray(new String[0]);
    }
}