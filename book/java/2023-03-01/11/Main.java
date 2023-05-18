import business.Employee;

class Main {
    public static void main(String[] args) {
        var employee = new Employee("Marco Polo", 1500);
        employee.raiseSalary(10);
        System.out.println(employee.getSalary());
    }
}
