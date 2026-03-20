class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        int count = 0;
        
        for (boolean f : finished) {
            if (!f) count++;
        }
        
        String[] ans = new String[count];
        int idx = 0;
        
        for (int i = 0; i < todo_list.length; i++) {
            if (!finished[i]) {
                ans[idx++] = todo_list[i];
            }
        }
        
        return ans;
    }
}