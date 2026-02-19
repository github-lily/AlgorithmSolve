import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int i = 0;
        Stack<Integer> stack = new Stack<>();
        
        while (i < arr.length) {
            if (stack.isEmpty() || stack.peek() < arr[i]) {
                stack.push(arr[i]);
                i++;
            } else {
                stack.pop();
            }
        }

        
        return stack.stream().mapToInt(x->x).toArray();
    }
}