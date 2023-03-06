import bugs.Bug;
import bugs.Moth;

class Main {
    public static void main(String[] args) {
        var bug = new Bug(10);
        System.out.println(bug.getPosition());

        for (int i = 0; i < 10; i++)
            bug.move();
        System.out.println(bug.getPosition());

        bug.turn();
        for (int i = 0; i < 29; i++)
            bug.move();
        System.out.println(bug.getPosition());

        System.out.println("\n\nMoth: ");

        var moth = new Moth(10);
        moth.moveToLight(0);
        System.out.println(moth.getPosition());
        moth.moveToLight(10);
        System.out.println(moth.getPosition());
        moth.moveToLight(0);
        System.out.println(moth.getPosition());
    }
}
