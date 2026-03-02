class Solution {
    public int solution(String my_string, String suffix) {
        for (int i = 0; i < my_string.length(); i++) {
            if (my_string.charAt(i) == suffix.charAt(0) ) {
                if ( my_string.substring(i).equals(suffix)) {
                    return 1;
                }
            }
        } return 0;
    }
}