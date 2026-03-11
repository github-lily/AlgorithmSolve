class Solution {
    int ans = 0;
    int[] arr;
    int N;
    int t;
    
    public int solution(int[] numbers, int target) {
       
        arr = numbers;
        N = numbers.length;
        t = target;
                    
        powerset(0,0);
        
        return ans;
    }
    
    public void powerset(int idx, int sum) {
        // 기저 조건
        if (idx >= N) {
            if (sum == t) {
                ans += 1;
            }
            return;
        }
        
        
        // 재귀 조건
        powerset(idx+1, sum+arr[idx]);
        powerset(idx+1, sum-arr[idx]);
        
    }
}