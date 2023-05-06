import java.util.Arrays;
import java.util.Scanner;

public class p2562 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] arr = new int[9];
        int max = 0;
        int idx = 0;

        for (int i = 0; i < 9; i++) {
            arr[i] = scanner.nextInt();
        }

        for (int i = 0; i < 9; i++) {
            if (max < arr[i]) {
                max = arr[i];
                idx = i;
            }
        }

        System.out.println(max);
        System.out.println(idx + 1);

        scanner.close();
    }
}
