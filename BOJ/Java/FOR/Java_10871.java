import java.util.Scanner;

public class Java_10871 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int x = input.nextInt();

        int[] lst = new int[n];
        for(int i = 0; i < n; i++){
            lst[i] = input.nextInt();
        }
        input.close();

        for(int j = 0; j < n; j++){
            if(lst[j] < x){
                System.out.println(lst[j] + " ");
            }
        }
    }
}
