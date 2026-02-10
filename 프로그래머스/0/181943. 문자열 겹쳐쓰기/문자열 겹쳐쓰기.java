class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        int my_len = my_string.length();
        int over_len = overwrite_string.length();

        String pre_char = my_string.substring(0,s);
        String post_char = my_string.substring(s+over_len, my_len);

        String ans = pre_char + overwrite_string + post_char;
        return ans;
    }
}