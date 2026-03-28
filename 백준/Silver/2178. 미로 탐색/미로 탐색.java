
import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[][] arr;
    static int[] di = {0,1,0,-1};   //우하좌상
    static int[] dj = {1,0,-1,0};

    public static void main(String[] args) throws IOException {
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];

        for (int i = 0; i < N ; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        bfs(0,0);
        System.out.println(arr[N-1][M-1]);

    }

    public static void bfs(int si, int sj) {

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {si,sj});

        while (!q.isEmpty()) {
            int[] c = q.poll();
            int ci = c[0];
            int cj = c[1];

            if (ci == N-1 && cj == M-1) {
                return;
            }

            for (int k = 0; k < 4; k++) {
                int ni = ci + di[k];
                int nj = cj + dj[k];
                if (ni >= 0 && ni < N && nj >= 0 && nj < M && arr[ni][nj] == 1) {
                    arr[ni][nj] = arr[ci][cj] + 1;
                    q.offer(new int[] {ni,nj});
                }
            }

        }
    }

}
