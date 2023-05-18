import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
   Used to test the FileTrimmer class.
*/
public class FileTrimmerTester
{
   public static void main(String[] args)
   {
      FileTrimmer.trimBlankLines("lines.txt");
      int count = 0;
      try (Scanner in = new Scanner(new File("lines.txt")))
      {
         while (in.hasNextLine())
         {
            in.nextLine();
            count++;
         }
      } 
      catch (FileNotFoundException e)
      {
         e.printStackTrace();
      }
      System.out.println("Number of remaining lines: " + count);
      System.out.println("Expected: 12");
   }
}
