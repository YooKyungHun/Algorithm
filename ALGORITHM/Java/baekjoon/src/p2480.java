import java.util.Scanner;

public class p2480 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int answer = 0;

        int max = 0;
//        if (a >= b) {
//            if (a > c) {
//                max = a;
//            } else {
//                max = c;
//            }
//        } else if (b < c) {
//            max = c;
//        } else {
//            max = b;
//        }

        max = Math.max(Math.max(a, b), c);

        if (a == b && b == c) {
            answer = 10000 + a * 1000;
        } else if (a != b && b != c && a != c) {
            answer = max * 100;
        } else if (a == b) {
            answer = 1000 + a * 100;
        } else if (b == c) {
            answer = 1000 + b * 100;
        } else if (c == a) {
            answer = 1000 + c * 100;
        }

        System.out.println(answer);
        sc.close();
    }
}
