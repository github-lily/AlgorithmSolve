class Solution {
    String alphabet = "AEIOU";
    int N = alphabet.length();
    String target;
    int cnt = 0;
    boolean found = false;
    
    public void dfs(String w) {
        if (found) return;
        if (w.equals(target)) {
            found = true;
            return;
        }
        if (w.length() == N) return;
        
        for (int i = 0; i < N; i++) {
            cnt += 1;
            dfs(w+alphabet.charAt(i));
            
            if (found) return;
        }
    }
    
    
    public int solution(String word) {
        target = word;
        dfs("");
        return cnt;
    }
}