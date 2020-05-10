import java.util.Scanner;

public class Java_10951 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while(input.hasNextInt()){
            int a = input.nextInt();
            int b = input.nextInt();

            System.out.println(a + b);
        }
    }
}
