class Solution {
    String[] alphabet = {"A", "E", "I", "O", "U"}; 
    int cnt = 0; 
    int answer = 0; 
    boolean found = false; 
    String target;

    public int solution(String word) {
        target = word;
        dfs("");
        return answer; 
    }

    public void dfs(String w) {
        if (found) return; 

        // 현재 문자열이 빈 문자열이 아닐 때만 카운트
        if (!w.equals("")) {
            cnt++;
        }

        // 찾으면 answer 저장 후 종료
        if (w.equals(target)) {
            answer = cnt;
            found = true;
            return;
        }

        // 기저조건
        if (w.length() == 5) return;

        // 재귀 부분
        for (int i = 0; i < 5; i++) {
            dfs(w + alphabet[i]);
        }
    }
}