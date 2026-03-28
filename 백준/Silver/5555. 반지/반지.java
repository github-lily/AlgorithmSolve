
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String text = br.readLine();
        int N = Integer.parseInt(br.readLine());
        int ans = 0;


        for (int i = 0; i < N; i++) {
            String ring = br.readLine();
            String doubled = ring + ring; // 원형 처리

            boolean isRing = false;

            for (int j = 0; j < ring.length(); j++) {
                int t = 0;

                while (t < text.length()) {
                    if (doubled.charAt(j + t) != text.charAt(t)) {
                        break;
                    }
                    t++;
                }

                // 전부 일치
                if (t == text.length()) {
                    isRing = true;
                    break;
                }

            }
            if (isRing) ans++;
        }

        System.out.println(ans);
    }

}

