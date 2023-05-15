import java.util.Arrays;
import java.util.Scanner;

/**
   This program tests the binary search algorithm.
*/
public class BinarySearchTester
{
   public static void main(String[] args)
   {
      String[] words =
      {
         "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
         "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike",
         "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra",
         "Tango", "Uniform", "Victor", "Whiskey", "X-Ray", "Yankee",
         "Zulu"
      };
      BinarySearcher<String> searcher = new BinarySearcher<>(words);
      System.out.println(searcher.search("November"));
      System.out.println("Expected: 13");
      System.out.println(searcher.search("October"));
      System.out.println("Expected: -1");
   }
}
