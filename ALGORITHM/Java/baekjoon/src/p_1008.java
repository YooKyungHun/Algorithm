import java.util.Scanner;

public class p_1008 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        double answer = (double)A / B;

        System.out.println(answer);
        sc.close();
    }
}