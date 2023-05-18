import java.util.ArrayList;

/**
   This program demonstrates reversing an arraylist
*/
public class ReverseTester
{
   public static void main(String[] args)
   {
      ArrayList<String> a = new ArrayList<>();
      a.add("apple");
      a.add("orange");
      a.add("pear");
      a.add("banana");
      ArrayList<String> b = ArrayListUtil.reverse(a);

      System.out.println("Original: " + a);
      System.out.println("Expected: [apple, orange, pear, banana]");
      System.out.println("Reversed: " + b);
      System.out.println("Expected: [banana, pear, orange, apple]");
   }

}
