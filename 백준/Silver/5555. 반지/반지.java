import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String target = br.readLine();
        int n = Integer.parseInt(br.readLine());

        int ans = 0;

        for (int tc = 0; tc < n; tc++) {
            String ring = br.readLine();
            String doubled = ring+ring;     // 원형 반지임을 고려(처음과 끝이 만남)

            if (doubled.contains(target)) {
                ans++;
            }

        }
        System.out.println(ans);
    }

}
