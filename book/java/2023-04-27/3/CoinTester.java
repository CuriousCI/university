/**
 * This program demonstrates the Comparable coin class.
 */
public class CoinTester {
   public static void main(String[] args) {
      Comparable coin1 = new Coin(.25, "Quarter");
      Comparable coin2 = new Coin(.10, "Dime");
      Comparable coin3 = new Coin(.10, "Dime");

      System.out.println(coin1.compareTo(coin2));
      System.out.println("Expected: 1");
      System.out.println(coin2.compareTo(coin3));
      System.out.println("Expected: 0");
      System.out.println(coin3.compareTo(coin1));
      System.out.println("Expected: -1");
   }
}
