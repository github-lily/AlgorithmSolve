class Solution {
    public int[] solution(int n, int k) {
        int[] ans = new int[n/k];
        
        for (int i = 1; i*k <= n; i++) {
            ans[i-1] = i*k;
        }
        
        return ans;
    }
}