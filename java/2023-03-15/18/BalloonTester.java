
public class BalloonTester {

    public static void main(String[] args) {
         
      Balloon balloon = new Balloon();
      
      balloon.addAir(100);
      System.out.println("Volume: " + balloon.getVolume());
      System.out.println("Expected: 100.0");
      System.out.println("Surface Area: " + balloon.getSurfaceArea());
      System.out.println("Expected: 104.187942");
      System.out.println("Radius: " + balloon.getRadius());
      System.out.println("Expected: 2.879412");
      
      balloon.addAir(100);
      System.out.println("Volume: " + balloon.getVolume());
      System.out.println("Expected: 200.0");
      System.out.println("Surface Area: " + balloon.getSurfaceArea());
      System.out.println("Expected: 165.388048");
      System.out.println("Radius: " + balloon.getRadius());
      System.out.println("Expected: 3.627832");
    }
}
