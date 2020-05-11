import java.util.Scanner;

public class Java_1110 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int x = n;
        int cnt = 0;

        while(true){
            int a = n / 10;
            int b = n % 10;

            n = (b * 10) + ((a + b) % 10);
            cnt ++;
            if(n == x){
                System.out.println(cnt);
                break;
            }
        }
    }
}
