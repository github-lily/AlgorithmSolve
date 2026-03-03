
class Solution {
    public String solution(String my_string, int s, int e) {
        // 문자열 뒤집기
        StringBuilder temp = new StringBuilder();
        temp.append(my_string.substring(s,e+1));
        temp.reverse();
        
        // 합치기
        StringBuilder ans = new StringBuilder();
        ans.append(my_string.substring(0,s));
        ans.append(temp);
        ans.append(my_string.substring(e+1));
        
        return ans.toString();
    }
}