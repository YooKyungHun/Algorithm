import java.util.Scanner;

public class p2525 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int inputHour = sc.nextInt();
        int inputMinute = sc.nextInt();
        int cookingTime = sc.nextInt();

        int outputHour = inputHour + cookingTime / 60;;
        int outputMinute = inputMinute + cookingTime % 60;;

        if (outputMinute >= 60) {
            outputMinute -= 60;
            outputHour++;
        }

        outputHour %= 24;

        System.out.println(outputHour);
        System.out.println(outputMinute);

        sc.close();
    }

}
