import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long n = sc.nextLong();
        
        long totalSum = 0;

        for (long r = 1; r < n; r++) {
            totalSum += (n * r) + r;
        }

        System.out.println(totalSum);
    }
}