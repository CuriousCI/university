/**
   Tests bag functionality.
*/
public class BagTester
{
   public static void main(String[] args)
   {
      Bag bag = new Bag();

      bag.add("car");
      bag.add("tree");
      bag.add("car");
      bag.add("tree");
      bag.add("shoe");
      bag.add("tree");

      System.out.println("Shoes: " + bag.count("shoe"));
      System.out.println("Expected: 1");
      System.out.println("Cars: " + bag.count("car"));
      System.out.println("Expected: 2");
      System.out.println("Trees: " + bag.count("tree"));
      System.out.println("Expected: 3");
      System.out.println("Lights: " + bag.count("light"));
      System.out.println("Expected: 0");
   }
}
