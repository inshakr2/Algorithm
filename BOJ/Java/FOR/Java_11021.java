import java.util.Scanner;

public class Java_11021 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();
        for(int i = 1; i <= T; i++){
            int x = input.nextInt();
            int y = input.nextInt();
            System.out.println("Case #" + i + ": " + (x + y));
        }
    }
}
