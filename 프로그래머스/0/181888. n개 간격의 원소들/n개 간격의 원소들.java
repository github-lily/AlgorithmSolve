import java.util.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = 0; i < num_list.length; i+= n) {
            ans.add(num_list[i]);
        } return ans.stream().mapToInt(i->i).toArray();
    }
}