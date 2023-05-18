import java.awt.Color;
import java.util.Map;
import java.util.Set;

/**
   This program tests a map that maps names to colors.
*/
public class MapTester
{
   public static void main(String[] args)
   {
      HashMap<String, Color> favoriteColors =  new HashMap<>();
      favoriteColors.put("Juliet", Color.PINK);
      favoriteColors.put("Romeo", Color.GREEN);
      favoriteColors.put("Adam", Color.BLUE);
      favoriteColors.put("Eve", Color.PINK);
      favoriteColors.put("Romeo", Color.WHITE);
      favoriteColors.remove("Juliet");
      System.out.println(favoriteColors.get("Romeo"));
      System.out.println("Expected: java.awt.Color[r=255,g=255,b=255]");
      System.out.println(favoriteColors.get("Juliet"));
      System.out.println("Expected: null");
      System.out.println(favoriteColors.size());
      System.out.println("Expected: 3");
      Set<String> keys = favoriteColors.keySet();
      System.out.println(keys.size());
      System.out.println("Expected: 3");
   }
}
