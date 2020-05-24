import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Java_2577 {
    private static int[] map = new int[10];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        int[] input = new int[3];
        int mul = 1;
        for (int i = 0; i < 3; i++) {
            mul *= Integer.parseInt(br.readLine().trim());
        }

        map[mul % 10]++;

        while (true) {
            mul /= 10;
            map[mul % 10]++;

            if (mul < 10) {
                break;
            }
        } for (int i = 0; i < 10; i++) {
            System.out.println(map[i]);
        }
    }
}
