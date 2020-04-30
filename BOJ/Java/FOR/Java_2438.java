import java.util.*;

public class Java_2438 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        StringBuilder lst = new StringBuilder();
        int N = input.nextInt();

        for (int i = 1; i <= N; i++){
            for (int j = 0; j < i; j++){
                lst.append("*");
            }lst.append("\n");
        }

        System.out.println(lst);
    }
}
