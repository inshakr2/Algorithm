import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Java_10996 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder A = new StringBuilder();
        StringBuilder B = new StringBuilder();

        if (N == 1) {
            System.out.println("*");
        } else {
            if (N % 2 == 0) {
                for (int i = 0; i < (N / 2); i++) {
                    A.append("* ");
                    B.append(" *");
                }
            } else {
                for (int i = 0; i < (N / 2); i++) {
                    A.append("* ");
                    B.append(" *");
                }
                A.append("*");
            }
        }
        for(int i = 0; i < N; i++){
            System.out.println(A);
            System.out.println(B);
        }
    }
}
