class Solution {
    public String solution(String code) {
        StringBuilder answer = new StringBuilder();
        int mode = 0;

        for (int i = 0; i < code.length(); i++) {
            char c = code.charAt(i);

            if (c == '1') {
                mode = 1 - mode; // mode 토글
            } else {
                if (mode == 0 && i % 2 == 0) {
                    answer.append(c);
                } else if (mode == 1 && i % 2 == 1) {
                    answer.append(c);
                }
            }
        }

        return answer.length() == 0 ? "EMPTY" : answer.toString();
    }
}
