import java.util.Scanner;

public class Java_2739 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();

        for(int y = 1; y < 10; y++){
            System.out.println(x + " * " + y + " = " + x * y);
        }
    }
}
