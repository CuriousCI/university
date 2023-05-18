import java.lang.StringBuilder;

class Main {
    public static void main(String[] args) {
        // Ex 1
        var mississippi = "Mississippi";
        System.out.println(mississippi.replace("i", "ii").replace("ss", "s"));

        // Ex 2
        var spaces = "    jakljkla kajs askjdl   jkalsj alkj a lkjkj    ";
        System.out.println(spaces.trim().replace(" ", ""));

        // Ex 7
        System.out.println(mississippi.replace('i', '!').replace('s', '$'));

        // Ex 8
        var hello = "Hello, World!";
        System.out.println(hello.replace('e', '%').replace('o', 'e').replace('%', 'o'));

        // Ex 9
        var d = new StringBuilder("desserts");
        System.out.println(d.reverse());
    }
}
