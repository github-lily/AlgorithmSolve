class Solution {
    public String solution(String str1, String str2) {
        int n = str1.length();
        String ans = "";
        
        for (int i = 0; i < n; i++) {
            ans += str1.charAt(i);
            ans += str2.charAt(i);
        }
        return ans;
    }
}