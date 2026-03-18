class Solution {
    public int[] solution(int[] arr) {
        
        int N = arr.length;
        int start = 0;
        int end = 0;
        boolean exist = false;
        
        // 시작점 찾기
        for (int i = 0; i < N; i++) {
            if (arr[i] == 2) {
                start = i;
                exist = true;
                break;
            }
        }
        
        // 2가 있을 때만 끝점 찾기
        if (exist) {
            for (int j = N-1; j >= start; j--) {
                if (arr[j] == 2) {
                    end = j;
                    break;
                }
            } 
            
            // 구간 추출
            int[] result = new int[end - start + 1];
            for (int s = start; s <= end; s++) {
                result[s-start] = arr[s];
            }
            return result;
        }
        
        // 없으면 -1 반환
        
        return new int[]{-1};
    }
}