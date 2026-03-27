
import java.io.*;
import java.util.*;

public class Main {

    static int N,M;
    static int[][] arr;
    static int[] dr = {0,1,0,-1};      // 우하좌상
    static int[] dc = {1,0,-1,0};

    public static void main(String[] args) throws IOException {
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];


        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;
        int maxArea = 0;

        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 1) {
                    ans++;

                    int area = bfs(i,j);

                    maxArea = Math.max(maxArea,area);
                }
            }
        }

        System.out.println(ans);
        System.out.println(maxArea);
    }

    static int bfs(int r, int c) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {r,c});

        arr[r][c] = 0;
        int area = 1;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cr = cur[0];
            int cc = cur[1];

            for (int k = 0; k<4; k++) {
                int nr = cr + dr[k];
                int nc = cc + dc[k];

                if (nr >= 0 && nr < N && nc >= 0 && nc < M && arr[nr][nc] == 1) {
                    arr[nr][nc] = 0;
                    q.offer(new int[]{nr,nc});
                    area++;
                }
            }
        }
        return area;
    }

}
