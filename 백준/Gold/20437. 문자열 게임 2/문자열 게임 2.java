
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            String words = br.readLine();
            int K = Integer.parseInt(br.readLine());

            int mn = 10001;
            int mx = 0;

            List<Integer>[] idxs = new ArrayList[26];
            for (int i = 0; i < 26; i ++ ) {
                idxs[i] = new ArrayList<>();
            }
            for (int i = 0; i < words.length(); i++) {
                int cur = (int) words.charAt(i) - 97;
                idxs[cur].add(i);
            }

            for (List<Integer> idx : idxs) {
                for (int i = 0; i < idx.size() - K + 1; i++ ) {
                    int len = idx.get(i + K - 1) - idx.get(i) +1;
                    mn = Math.min(mn,len);
                    mx = Math.max(mx,len);
                }
            }

            if (mn == 10001 && mx == 0) {
                System.out.println(-1);
            } else {
                System.out.println(mn + " " + mx);
            }
        }
    }

}
