class Solution {
    public int solution(int a, int b, int c) {
        // 모두 같을 때
        if (a == b && b == c) {
            return (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c);
        // 모두 다를 때
        } else if (a != b && b != c && a != c) {
            return (a + b + c);
        // 나머지
        } else {
            return (a + b + c) * (a*a + b*b + c*c);
        } 
    }
}