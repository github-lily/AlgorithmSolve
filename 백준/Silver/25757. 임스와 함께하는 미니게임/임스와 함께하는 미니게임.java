import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Set<String> set = new HashSet<>();


        int N = Integer.parseInt(st.nextToken());
        String game = st.nextToken();

        for (int i = 0; i < N; i++) {
            set.add(br.readLine());
        }

        int divisor = 0;

        switch (game) {
            case "Y" : divisor = 1; break;
            case "F" : divisor = 2; break;
            case "O" : divisor = 3; break;
        }

        int ans = set.size() / divisor;
        System.out.println(ans);
    }
}
