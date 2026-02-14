class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] ans = new int[n+1];

        for (int i = 0; i < n; i++) {
            ans[i] = num_list[i];
        }
        
        if (n == 1) {
            return ans;
        }
        
        

        int last_one = num_list[n-1];
        int last_two = num_list[n-2];
         
        if (last_one > last_two) {      // 끝 값이 큰 경우
            ans[n] = last_one - last_two;
        } else {
            ans[n] = last_one * 2;      // 끝 값이 작은 경우
        }
        
        return ans;
    }
}