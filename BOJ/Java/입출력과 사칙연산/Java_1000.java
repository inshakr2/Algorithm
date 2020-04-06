import java.util.Scanner;

public class Java_1000 {
    public static void main(String[] args) {
        int a;
        int b;
        try (Scanner data = new Scanner(System.in)) {

            a = data.nextInt();
            b = data.nextInt();
        }

        System.out.println(a + b);
    }
}
