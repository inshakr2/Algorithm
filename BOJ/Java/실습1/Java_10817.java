import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.util.Arrays;

public class Java_10817 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] pre_lst = br.readLine().split(" ");
        int[] lst = new int[3];

        for(int i = 0; i < 3; i++){
            lst[i] = Integer.parseInt(pre_lst[i]);
        }


        Arrays.sort(lst);
        System.out.println(lst[1]);

    }
}
