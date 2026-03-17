class Solution {
    public int[] solution(int[] arr) {
        int start = -1;
        int end = -1;

        // 첫 번째 2 찾기
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                start = i;
                break;
            }
        }

        // 마지막 2 찾기
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] == 2) {
                end = i;
                break;
            }
        }

        // 2가 없는 경우
        if (start == -1) {
            return new int[]{-1};
        }

        // 구간 추출
        int[] result = new int[end - start + 1];
        for (int i = start; i <= end; i++) {
            result[i - start] = arr[i];
        }

        return result;
    }
}