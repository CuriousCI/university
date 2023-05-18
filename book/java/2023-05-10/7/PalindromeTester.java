import java.util.ArrayList;
import java.awt.Color;

/**
 * This program demonstrates checking if a generic ArrayList
 * is a palindrome.
 */
public class PalindromeTester {
    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList<>();
        a.add("apple");
        a.add("orange");
        a.add("apple");

        System.out.println("A: " + ArrayListUtil.isPalindrome(a));
        System.out.println("Expected: true");

        ArrayList<String> b = new ArrayList<>();
        b.add("pear");
        b.add("banana");

        System.out.println("B: " + ArrayListUtil.isPalindrome(b));
        System.out.println("Expected: false");

        ArrayList<Color> c = new ArrayList<>();
        c.add(Color.RED);
        c.add(Color.GREEN);
        c.add(Color.BLUE);
        c.add(Color.GREEN);
        c.add(Color.RED);

        System.out.println("C: " + ArrayListUtil.isPalindrome(c));
        System.out.println("Expected: true");

        ArrayList<Frutto> f = new ArrayList<>();
        f.add(new Frutto("apple"));
        f.add(new Frutto("banana"));
        f.add(new Frutto("apple"));
        System.out.println(ArrayListUtil.isPalindrome(f));
    }

}

class Frutto {
    String nome;

    public Frutto(String nome) {
        this.nome = nome;
    }
}
