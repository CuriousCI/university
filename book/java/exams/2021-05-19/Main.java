public class Main {
    public static void main(String[] args) {
        var p = new Person("Marco");
        System.out.println(p.toJson());

    }
}

interface Serializable {
    String toJson();

}

class Person implements Serializable {
    String name;

    public Person(String name) {
        this.name = name;
    }

    @Override
    public String toJson() {
        return String.format("{name: \"%s\"}", name);
    }
}
