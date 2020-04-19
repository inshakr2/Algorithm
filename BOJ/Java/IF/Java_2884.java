import java.util.Scanner;

public class Java_2884 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int H = input.nextInt();
        int M = input.nextInt();

        M -= 45;

        if(M < 0){
            M += 60;
            H -= 1;
            if(H < 0){
                H = 23;
            }
        }
        System.out.println(H+ " " + M);
    }
}
