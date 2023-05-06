import java.util.Scanner;

public class p2753 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int year = scanner.nextInt();
        int answer;

        if (year % 4 == 0 && year % 100 != 0) {
            answer = 1;
        } else if (year % 400 == 0) {
            answer = 1;
        } else {
            answer = 0;
        }

        System.out.println(answer);

        scanner.close();
    }
}
