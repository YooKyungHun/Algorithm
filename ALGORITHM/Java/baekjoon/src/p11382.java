import java.util.Scanner;

public class p11382 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long A = sc.nextLong();
        long B = sc.nextLong();
        long C = sc.nextLong();

        long answer = A + B + C;

        System.out.println(answer);

        sc.close();
    }
}
