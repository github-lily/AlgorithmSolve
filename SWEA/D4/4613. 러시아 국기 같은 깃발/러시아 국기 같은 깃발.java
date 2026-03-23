
import java.io.*;
import java.util.*;

class Solution {

    public static void main(String[] args) throws IOException {

        StringBuilder sb = new StringBuilder();
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++ ) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            char[][] arr = new char[N][M];

            for (int i = 0; i<N; i++) {
                String line = br.readLine();
                for (int j = 0; j<M; j++) {
                    arr[i][j] = line.charAt(j);
                }
            }

            int[][] cost = new int[N][3];

            for (int r=0; r < N; r++) {
                int WCnt = 0;
                int BCnt = 0;
                int RCnt = 0;

                for (int c=0; c<M; c++) {
                    switch (arr[r][c]) {
                        case 'W' :
                            WCnt++;
                            break;
                        case 'B' :
                            BCnt++;
                            break;
                        case 'R' :
                            RCnt++;
                            break;
                    }
                }

                // 각 색으로 바꾸는데 드는 비용
                cost[r][0] = M - WCnt;
                cost[r][1] = M - BCnt;
                cost[r][2] = M - RCnt;

            }

            int ans = Integer.MAX_VALUE;

            for (int startBlue = 1; startBlue <= N-2; startBlue++ ) {
                for (int startRed = startBlue+1; startRed <= N-1; startRed++) {
                    int sum = 0;
                    // 각 색상으로 바꾸는 비용 계산
                    for (int i = 0; i < startBlue; i++) {
                        sum += cost[i][0];
                    }

                    for (int i = startBlue; i < startRed; i++) {
                        sum += cost[i][1];
                    }

                    for (int i = startRed; i <= N - 1; i++) {
                        sum += cost[i][2];
                    }

                    ans = Math.min(ans, sum);
                }
            }

            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
    System.out.print(sb);
    }
}