import java.util.Scanner;

public class p_9498 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double score = scanner.nextDouble();
        String grade;

        if (score >= 90) {
            grade = "A";
        } else if (score >= 80) {
            grade = "B";
        } else if (score >= 70) {
            grade = "C";
        } else if (score >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }
        System.out.println(grade);
        scanner.close();
    }
}
