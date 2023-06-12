import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;
import java.util.regex.PatternSyntaxException;

public class Main {
    public static void main(String[] args) {

        try {
            Course course = Course.getFromFile(getFileName());

            System.out.println("Studenti con voto verbalizzato:");
            for (Student s : course.getRegisteredStudents())
                System.out.println(s);
            System.out.println();

            System.out.println("Studenti senza voto verbalizzato:");
            for (Student s : course.getUnregisteredStudents())
                System.out.println(s);
            System.out.println();

            System.out.printf(
                    "Statistiche corso:\n- numero studenti: %d\n- voto medio: %.2f\n- numero studenti che hanno passato l'esame: %d",
                    course.studentsCount(),
                    course.getAverageGrade(),
                    course.passedStudentsCount());

        } catch (InputMismatchException e) {
            System.err.println("File has incorrect format");
        } catch (FileNotFoundException e) {
            System.err.println("File not found");
        }
    }

    public static String getFileName() throws InputMismatchException {
        Scanner stdin = new Scanner(System.in);
        String filename;

        System.out.println("Filename: ");
        try {
            filename = stdin.next();
        } finally {
            stdin.close();
        }

        return filename;
    }
}

class Course {
    private List<Student> students;

    private Course() {
        this.students = new ArrayList<>();
    }

    public static Course getFromFile(String filename)
            throws FileNotFoundException, InputMismatchException {
        Course course = new Course();

        Scanner file = new Scanner(new File(filename));
        try {
            while (file.hasNextLine()) {
                Scanner line = new Scanner(file.nextLine());
                line.useDelimiter(":");

                String code = line.next();
                String name = line.next();
                String surname = line.next();
                Integer grade = line.hasNextInt() ? line.nextInt() : 0;

                course.students.add(new Student(code, name, surname, grade));
            }
        } finally {
            file.close();
        }

        return course;
    }

    public List<Student> getRegisteredStudents() {
        List<Student> registered = new ArrayList<>();

        for (Student student : this.students) {
            if (student.getGrade() != 0) {
                registered.add(student);
            }
        }

        return registered;
    }

    public List<Student> getUnregisteredStudents() {
        List<Student> unregistered = new ArrayList<>();

        for (Student student : this.students) {
            if (student.getGrade() == 0) {
                unregistered.add(student);
            }
        }

        return unregistered;
    }

    public int studentsCount() {
        return this.students.size();
    }

    public double getAverageGrade() {
        double gradesTotal = 0;
        double gradesCount = 0;

        for (Student student : this.students) {
            if (student.getGrade() != 0) {
                gradesTotal += student.getGrade();
                gradesCount++;
            }
        }

        if (gradesCount == 0)
            return 0;

        return gradesTotal / gradesCount;
    }

    public int passedStudentsCount() {
        return this.getRegisteredStudents().size();
    }
}

class Student {
    private String code;
    private String firstName;
    private String lastName;
    private int grade;

    public Student(String code, String firstName, String lastName, int grade) {
        this.code = code;
        this.firstName = firstName;
        this.lastName = lastName;
        this.grade = grade;
    }

    public Integer getGrade() {
        return this.grade;
    }

    @Override
    public String toString() {
        return String.format(
                "Code: %s\nStudent: %s %s\nGrade: %s\n",
                this.code,
                this.firstName,
                this.lastName,
                this.grade == 0 ? "non verbalizzato" : this.grade);
    }
}
