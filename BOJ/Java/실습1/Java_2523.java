import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Arrays;

public class Java_2523 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] lst = br.readLine().split(" ");
        int[] res = new int[5];

        for(int i = 0; i < 5; i++){
            res[i] = Integer.parseInt(lst[i]);
        }
    }
}
