class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int n = queries.length;
        int[] ans = new int[n];
        
        for (int i = 0; i < n; i++) {
            int mn = 9999999;
            int[] query = queries[i];
            int k = query[2];
            for (int j = query[0]; j <=query[1]; j++) {
                if (k < arr[j] && arr[j] < mn) {
                    mn = arr[j];
                }
            int temp = (mn == 9999999) ? -1 : mn ;
            ans[i] = temp;
            }
        } return ans;
    }
}