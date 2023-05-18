import cars.Car;

class Main {
    public static void main(String[] args) {
        var car = new Car(50);
        car.addGas(50);
        car.drive(100);

        System.out.println(car.getGasInTank());
    }
}
