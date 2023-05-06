import java.util.Scanner;

public class p2884 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int hour = scanner.nextInt();
        int minute = scanner.nextInt();

        int setHour = hour;
        int setMinute = minute - 45;

        if (setMinute < 0) {
            setMinute = 60 + setMinute;
            setHour--;
        }

        if (setHour < 0) {
            setHour = 23;
        }

        System.out.println(setHour);
        System.out.println(setMinute);

        scanner.close();
    }
}
