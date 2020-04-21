import java.util.Scanner;

public class Java_10950 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int to = input.nextInt();

        for(int i = 0; i < to; i++){
            int x = input.nextInt();
            int y = input.nextInt();
            System.out.println(x + y);
        }
    }
}
