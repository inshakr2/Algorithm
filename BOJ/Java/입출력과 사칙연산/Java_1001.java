import java.util.Scanner;

public class Java_1001 {
    public static void main(String[] args) {
        int a;
        int b;

        try (Scanner input = new Scanner(System.in)){

            a = input.nextInt();
            b = input.nextInt();
        }

        System.out.println(a - b);


    }
}
