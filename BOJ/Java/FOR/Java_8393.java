import java.util.Scanner;

public class Java_8393 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int to = input.nextInt();
        int res = 0;

        for(int i = 1; i <= to; i++){
            res += i;
        }
        System.out.println(res);
    }
}
