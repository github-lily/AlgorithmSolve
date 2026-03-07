import java.util.*;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        ArrayList<Integer> ans = new ArrayList<>();

        switch(n) {
            case 1 -> {
                for (int i = 0; i <= slicer[1]; i++) {
                    ans.add(num_list[i]);
                }
            }
            case 2 -> {
                for (int i = slicer[0]; i < num_list.length; i++) {
                    ans.add(num_list[i]);
                }
            }
            case 3 -> {
                for (int i = slicer[0]; i <= slicer[1]; i++) {
                    ans.add(num_list[i]);
                }
            }
            case 4 -> {
                for (int i = slicer[0]; i <= slicer[1]; i += slicer[2]) {
                    ans.add(num_list[i]);
                }
            }
        }
        return ans.stream().mapToInt(i->i).toArray();
    }
}