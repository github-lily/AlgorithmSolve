class Solution {
    public int solution(int[] num_list) {
        StringBuilder even = new StringBuilder();
        StringBuilder odd = new StringBuilder();
        
        for (int num : num_list) {
            (num % 2 == 0 ? even : odd).append(num);
        } 
        
        return Integer.parseInt(even.toString()) + Integer.parseInt(odd.toString());
    }
}