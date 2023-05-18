import school.*;

class Main {
    public static void main(String[] args) {
        var student = new Student(5);

        student.addScore(5.0);
        student.addScore(12.1802);
        student.addScore(42.98);
        student.addScore(2.2);

        student.removeMin();
        System.out.println(student.minimum());
    }
}
