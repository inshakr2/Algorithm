import java.util.Scanner;

public class Java_10039 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] scores = new int[5];
        for (int i = 0; i < scores.length; i++) {
            scores[i] = sc.nextInt();
        }
        sc.close();

        int sum = 0;
        for (int i = 0; i < scores.length; i++) {
            sum += scores[i] >= 40 ? scores[i] : 40;
        }
        System.out.println(sum / 5);
    }
}