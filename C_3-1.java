public class Main{
    public static void main(string[] args) {
        int n = 1260
        int cnt = 0;
        int[] coinTypes = {500, 100, 50, 10};

        for (int i = 0; i < n; i ++){
            int coin = coinTypes[i];
            cnt+= (n/coin);
            n %= coin;

        }

    }

}