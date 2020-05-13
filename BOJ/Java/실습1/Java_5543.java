import java.util.Scanner;

public class Java_5543 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);

        int burger = 2001;
        int drink = 2001;

        for(int i = 0; i < 3; i++){
            int tmp = input.nextInt();

            if(tmp < burger){
                burger = tmp;
            }
        }

        for(int i = 0; i < 2; i++){
            int tmp = input.nextInt();

            if(tmp < drink){
                drink = tmp;
            }
        }

        System.out.println(burger + drink - 50);
    }
}
