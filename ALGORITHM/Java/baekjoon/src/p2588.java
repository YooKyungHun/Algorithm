import java.util.Scanner;

public class p2588 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        int a = num2 / 100;
        int b = num2 % 100 / 10;
        int c = num2 % 100 % 10;

        System.out.println(num1 * c);
        System.out.println(num1 * b);
        System.out.println(num1 * a);
        System.out.println(num1 * num2);
        sc.close();
    }
}
