class Solution {
    public int solution(int[] num_list) {
        // length : 배열 길이 / length() : 문자열 길이 / size() : array, set 길이
        for (int i = 0; i < num_list.length; i ++) {
            if (num_list[i] < 0 ) {
                return i;
            } 
        }
        return -1;
    }
}