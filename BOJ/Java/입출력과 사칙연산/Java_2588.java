import java.util.Scanner;

public class Java_2588 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();

        System.out.println(a * (b%10));
        System.out.println(a* ((b/10)%10));
        System.out.println(a* (b/100));
        System.out.println(a*b);
    }

}
