class Solution {
    public String solution(int q, int r, String code) {
        StringBuilder ans = new StringBuilder();
        for (int i = r; i < code.length(); i += q) {
            ans.append(code.charAt(i));
        }
        
        return ans.toString();
    }
}