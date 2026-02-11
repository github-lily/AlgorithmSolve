class Solution {
    public String solution(String my_string, int n) {
        int my_len = my_string.length();
        return my_string.substring((my_len - n), my_len );
    }
}