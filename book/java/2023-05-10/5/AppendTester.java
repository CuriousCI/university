import java.util.ArrayList;

/**
   This program demonstrates appending two ArrayLists.
*/
public class AppendTester
{
   public static void main(String[] args)
   {
      ArrayList<String> a = new ArrayList<>();
      ArrayList<String> b = new ArrayList<>();
      a.add("apple");
      a.add("orange");
      b.add("pear");
      b.add("banana");
      ArrayList<String> c = ArrayListUtil.append(a, b);
      System.out.println("a: " + a);
      System.out.println("Expected: [apple, orange]");
      System.out.println("b: " + b);
      System.out.println("Expected: [pear, banana]");
      System.out.println("c: " + c);
      System.out.println("Expected: [apple, orange, pear, banana]");
   }

}
