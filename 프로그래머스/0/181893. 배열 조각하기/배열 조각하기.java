import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        for (int idx = 0; idx < query.length; idx++) {
            ArrayList<Integer> ans = new ArrayList<>();
            
            int s,e;
            int q = query[idx];
            
            if (idx % 2 == 0) { 
                s = 0;
                e = q;
            } else {
                s = q;
                e = arr.length-1;
            }

            for (int i = s; i<= e; i++) {
                ans.add(arr[i]);
            }
            
            arr = ans.stream().mapToInt(x->x).toArray();
        }
        return arr;
    }
}