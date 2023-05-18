import java.util.Scanner;

import machines.*;

class Main {
    public static void main(String[] args) {
        var input = new Scanner(System.in);
        int bills, coins;
        double price, amount;

        try {
            System.out.println("Insert bills\n1) 1 dollar\n2) 5 dollars\n3) 10 dollars");
            bills = input.nextInt();

            System.out.println("Insert coins\n1) 25 cents\n2) 50 cents");
            coins = input.nextInt();

            System.out.println("Insert the product of the price");
            price = input.nextDouble() * 100;

            System.out.println("Insert given amount of money");
            amount = input.nextDouble() * 100;
        } finally {
            input.close();
        }

    }
}
