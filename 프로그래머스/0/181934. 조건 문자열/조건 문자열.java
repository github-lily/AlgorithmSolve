class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        String operator = ineq + eq;

        if (operator.equals(">=") ) {
            return (n >= m) ? 1 : 0;  
        } else if (operator.equals("<=")) {
            return (n <= m) ? 1 : 0;
        } else if (operator.equals(">!")) {
            return (n > m) ? 1 : 0;
        } else {
            return (n < m) ? 1 : 0;
        }
    
    }
}