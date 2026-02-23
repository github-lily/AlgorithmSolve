class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] cnt = new int[7]; // 주사위 눈(1~6) 빈도 카운트
        cnt[a]++; cnt[b]++; cnt[c]++; cnt[d]++;

        int p = 0, q = 0, r = 0; 
        int maxCnt = 0;

        for (int i = 1; i <= 6; i++) {
            if (cnt[i] > maxCnt) {
                maxCnt = cnt[i];
                p = i;
            }
        }

        if (maxCnt == 4) { 
            return 1111 * p;
        }

        if (maxCnt == 3) { 
            for (int i = 1; i <= 6; i++) {
                if (cnt[i] == 1) q = i;
            }
            return (int) Math.pow(10 * p + q, 2);
        }

        if (maxCnt == 2) {
            int first = 0, second = 0;
            for (int i = 1; i <= 6; i++) {
                if (cnt[i] == 2) {
                    if (first == 0) first = i;
                    else second = i;
                }
            }
            if (second != 0) { 
                return (first + second) * Math.abs(first - second);
            } else { 
                for (int i = 1; i <= 6; i++) {
                    if (cnt[i] == 1) {
                        if (q == 0) q = i;
                        else r = i;
                    }
                }
                return q * r;
            }
        }

        int min = 7;
        for (int i = 1; i <= 6; i++) {
            if (cnt[i] == 1) min = Math.min(min, i);
        }
        return min;
    }
}