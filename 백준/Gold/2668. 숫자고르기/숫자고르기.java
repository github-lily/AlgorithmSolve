
import java.io.*;
import java.util.*;



public class Main {
    static boolean[] v;
    static int[] nums;
    static ArrayList<Integer> ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        nums = new int[(N+1)];
        for (int i = 1; i < N+1; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        ans = new ArrayList<>();

        for (int i = 1; i < N+1; i++) {
            v = new boolean[(N+1)];
            dfs(i,i);
        }

        System.out.println(ans.size());
        for (int a : ans) {
            System.out.println(a);
        }
    }

    public static void dfs(int start, int cur) {
        v[cur] = true;
        int next = nums[cur];

        if (!v[next]) {
            dfs(start,next);
        }

        else {
            if(start == next) {
                ans.add(start);
            }
        }

    }

}
