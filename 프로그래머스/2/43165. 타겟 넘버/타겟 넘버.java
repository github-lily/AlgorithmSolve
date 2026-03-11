class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
    
    public int dfs(int[] arr, int t, int idx, int sum) {
        // 기저 조건
        if (idx >= arr.length) {
            return (sum == t) ? 1 : 0;
        }
        
        // 재귀
        return dfs(arr, t, idx+1, sum+arr[idx]) + dfs(arr,t,idx+1,sum-arr[idx]);
    }
}