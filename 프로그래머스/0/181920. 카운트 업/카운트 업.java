class Solution {
    public int[] solution(int start_num, int end_num) {
        int n = end_num - start_num + 1;
        int[] ans = new int[n];
        
        for (int i = 0; i < n; i++) {
            ans[i] += start_num + i;
        }
        return ans;
    }
}