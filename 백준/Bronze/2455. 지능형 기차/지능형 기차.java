import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cur = 0;
        int max = 0;

        for (int i = 0; i < 4 ; i++) {

            StringTokenizer st = new StringTokenizer(br.readLine());

            int off = Integer.parseInt(st.nextToken());
            int on = Integer.parseInt(st.nextToken());

            cur -= off;
            cur += on;

            if (max < cur) {
                max = cur;
            }

        }

        System.out.println(max);
    }
}
