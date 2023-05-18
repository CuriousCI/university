package cars;

public class Car {
    private double gas, efficiency;

    public Car(double efficiency) {
        this.efficiency = efficiency;
        gas = 0;
    }

    public void addGas(double gas) {
        this.gas += gas;
    }

    public void drive(double distance) {
        gas -= distance / efficiency;
    }

    public double getGasInTank() {
        return gas;
    }

}
