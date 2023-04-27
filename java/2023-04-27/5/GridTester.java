/**
   Tests grid functionality.
*/
public class GridTester
{
   public static void main(String[] args)
   {
      Grid grid = new Grid(3, 4);

      grid.add(2, 1, "shoe");
      grid.add(1, 2, "tree");
      grid.add(0, 1, "car");

      System.out.println(grid.getDescription(0, 1));
      System.out.println("Expected: car");
      System.out.println(grid.getDescription(1, 2));
      System.out.println("Expected: tree");
      System.out.println(grid.getDescription(2, 1));
      System.out.println("Expected: shoe");

      for (Grid.Location location : grid.getDescribedLocations())
      {
         System.out.print(location.getRow() + "," + location.getColumn() + " ");
      }
      System.out.println();

      System.out.println("Expected: 0,1 1,2 2,1 ");
   }
}
