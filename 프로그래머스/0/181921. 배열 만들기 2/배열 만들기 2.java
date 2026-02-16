import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        // 동적 배열 생성
        List<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < 64 ; i++) {
            int num = Integer.parseInt(Integer.toBinaryString(i)) * 5;
            
            if (l <= num && num <= r) {
                ans.add(num);
            } else if (num > r) {
                break;
            }
        }
        
        return ans.isEmpty() ? new int[]{-1} : ans.stream().mapToInt(i -> i).toArray();
    }
}
