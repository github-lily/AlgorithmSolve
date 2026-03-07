class Solution {
    public int[] solution(String my_string) {
        int[] ans = new int[52];
        
        for (char c : my_string.toCharArray()) {
            if (Character.isUpperCase(c)) {
                ans[c-'A']++;
            } else {
                ans[c-'a'+26]++; // 소문자는 대문자보다 26자 뒤
            }
        }
        return ans;
    }
}