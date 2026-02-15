class Solution {
    public String solution(int[] numLog) {
        StringBuilder ans = new StringBuilder();
        for (int i = 1; i < numLog.length; i++) {
            int diff = numLog[i] - numLog[i-1];
            switch (diff) {
                case 1 :
                    ans.append("w");
                    break;
                case -1 :
                    ans.append("s");
                    break;
                case 10 :
                    ans.append("d");
                    break;
                case -10 :
                    ans.append("a");
                    break;
            }
        }
        return ans.toString();
    }
}