import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        // 동적 배열 생성
        List<Integer> ans = new ArrayList<>();
        
        for (int i = l; i <= r; i++) {
            String str = String.valueOf(i);
            
            // 5, 0인지 확인
            boolean ok = true;
            for (int j=0; j < str.length(); j++) {
                if (str.charAt(j) != '5' && str.charAt(j) != '0') {
                    ok = false;
                    break;
                } 
            }
            if (ok) {
                ans.add(i);
            }
        }
        
        if (ans.size() == 0) {
            int[] result = new int[]{-1};
            return result;
        }
        
        // 형변환
        int[] result = new int[ans.size()];
        for (int idx = 0; idx < ans.size(); idx++) {
            result[idx] = ans.get(idx);
        }    
        return result;
    }
}
