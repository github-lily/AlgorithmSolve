class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] ans = new int[n];
        
        for (int i = 0; i < n; i++) {
            ans[i] = num_list[n-i-1];
        }
        
        return ans;
    }
}