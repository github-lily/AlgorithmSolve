import java.util.*;

class Solution {
    public String[] solution(String[] todo, boolean[] done) {
        ArrayList<String> ans = new ArrayList<>();
        for (int i = 0; i < todo.length; i++ ) {
            if (!done[i]) { //false면 담기
                ans.add(todo[i]);
            }
        }
        return ans.toArray(new String[0]);
    }
}