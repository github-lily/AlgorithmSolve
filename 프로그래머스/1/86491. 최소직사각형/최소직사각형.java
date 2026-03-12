class Solution {
    public int solution(int[][] sizes) {
        int w_mx = 0;
        int h_mx = 0;
        
        for (int[] size : sizes) {
            int w = size[0];
            int h = size[1];
            
            if (h > w) {
                int temp = w;
                w = h;
                h = temp;
            }
            
            if (w > w_mx) {
                w_mx = w;
            } 
            if (h > h_mx) {
                h_mx = h;
            }
        }
        
        return w_mx * h_mx;
    }
}