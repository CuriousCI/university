public class PairTester
{
   public static void main(String[] args)
   {
      Pair<String, Integer> p = new Pair<>("Lucky Number", 13);
      Pair<Integer, String> q = PairUtil.swap(p);
      System.out.println(q.getFirst());
      System.out.println("Expected: 13");
      System.out.println(q.getSecond());
      System.out.println("Expected: Lucky Number");
   }
}
