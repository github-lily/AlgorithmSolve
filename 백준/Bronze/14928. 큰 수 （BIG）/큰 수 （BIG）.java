import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String nStr = br.readLine();
        
        long remainder = 0;
        final int MOD = 20000303;

        for (int i = 0; i < nStr.length(); i++) {
            int digit = nStr.charAt(i) - '0';
            
            remainder = (remainder * 10 + digit) % MOD;
        }

        System.out.println(remainder);
    }
}