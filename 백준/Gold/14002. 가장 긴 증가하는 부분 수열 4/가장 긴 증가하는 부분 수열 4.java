
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] lst = new int[N+1];
        int[] dp = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            lst[i] = Integer.parseInt(st.nextToken());
        }

        // 최대 길이 계산
        for (int i = 1; i <= N; i++) {
            for (int j = 0; j < i; j++) {
                if (lst[j] < lst[i]) {
                    if (dp[j] +1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                    }
                }
            }
        }

        // 최대 길이 값 구하기
        int mx = 0;
        for (int i = 1; i <=N; i++) {
            if (dp[i] > mx) {
                mx = dp[i];
            }
        }

        // 최대 길이 배열 구하기
        int[] ans = new int[mx];
        int cur = mx;

        for (int i = N; i > 0; i-- ) {
            if (dp[i] == cur) {
                ans[cur-1] = lst[i];
                cur--;
                if (cur == 0) {
                    break;
                }
            }
        }

        System.out.println(mx);
        for (int x : ans) {
            System.out.println(x + " ");
        }


    }

}
